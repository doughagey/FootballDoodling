import tkinter as tk
import matplotlib.pyplot as plt
import os
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def click(e):
    # define start point for line
    coords["x"] = e.x
    coords["y"] = e.y

    # create a line on this point and store it in the list
    lines.append(canvas.create_line(coords["x"], coords["y"], coords["x"], coords["y"],fill='white'))

def doubleclick(e):
    # define start point for line
    coords["x"] = e.x
    coords["y"] = e.y

    # create a line on this point and store it in the list
    lines.append(canvas.create_line(coords["x"], coords["y"], e.x+1, e.y, fill='white'))

def drag(e):
    # update the coordinates from the event
    coords["x2"] = e.x
    coords["y2"] = e.y

    # Change the coordinates of the last created line to the new coordinates
    canvas.coords(lines[-1], coords["x"], coords["y"], coords["x2"], coords["y2"])

def actionList():
    playerid = player_input.get()
    teamid = team_input.get()
    matchid = match_input.get()
    event = event_input.get()
    phase_type = phase_input.get()
    eventList.append({'player':playerid,'teamid':teamid, 'matchid':matchid, 'event_type':event, 'phase_type':phase_type})
    eventList[len(eventList)-1].update(coords)
    #eventList.append(coords)
    print(eventList)

def update(variable):
    variable.get()

eventList = []
root = tk.Tk()

background_image=tk.PhotoImage(file="Pitch2.png")

root.resizable(width=True, height=True)
root.wm_attributes("-topmost", 1)
canvas = tk.Canvas(root, bg="white", width=690, height=560)


# This is the player textbox
player_text = tk.StringVar()
player_input = tk.Entry (root, textvariable=player_text,validate="focusout")
#e = Entry(root, textvariable=sv, validate="focusout", validatecommand=callback)
canvas.create_window(50, 530, window=player_input, width = 100)

playerLabel = tk.Label(root, text='Player Name/Id:')
playerLabel.config(font=('Arial', 10))
canvas.create_window(40, 500, window=playerLabel)

# This is the team textbox
team_text = tk.StringVar()
team_input = tk.Entry (root, textvariable=team_text,validate="focusout")
canvas.create_window(160, 530, window=team_input, width = 100)

teamLabel = tk.Label(root, text='Team Name/Id:')
playerLabel.config(font=('Arial', 10))
canvas.create_window(155, 500, window=teamLabel)

# This is the match textbox
match_input = tk.Entry (root)
canvas.create_window(270, 530, window=match_input, width = 100)

matchLabel = tk.Label(root, text='Match Name/Id:')
matchLabel.config(font=('Arial', 10))
canvas.create_window(260, 500, window=matchLabel)

# This is the event textbox
event_text = tk.StringVar()
event_input = tk.Entry (root,textvariable=event_text,validate="focusout")
canvas.create_window(380, 530, window=event_input, width = 100)

eventLabel = tk.Label(root, text='Event Type')
eventLabel.config(font=('Arial', 10))
canvas.create_window(360, 500, window=eventLabel)

# This is the phase type
phase_text = tk.StringVar()
phase_input = tk.Entry (root,textvariable=phase_text,validate="focusout")
phase_input.insert(0, "OpenPlay")
canvas.create_window(490, 530, window=phase_input, width = 100)

phaseLabel = tk.Label(root, text='Phase Type')
phaseLabel.config(font=('Arial', 10))
canvas.create_window(470, 500, window=phaseLabel)

# This is the button to submit
submit_button = tk.Button(text='Submit', command=actionList)
canvas.create_window(600, 530, window=submit_button)

# End of regular stuff
canvas.pack(fill=tk.BOTH, expand=1) # Stretch canvas to root window size.
image = canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

coords = {"x":0,"y":0,"x2":0,"y2":0}
# keep a reference to all lines by keeping them in a list
lines = []
dots = []
canvas.bind("<ButtonPress-1>", click)
canvas.bind("<B1-Motion>", drag)
canvas.bind('<Double-Button-1>', doubleclick)

canvas.configure(scrollregion=canvas.bbox("all"))

root.mainloop()
graph = input('Do you want to view your graph (y/n)?: ')


if graph == 'y':
    #title = input('Please enter a title for the graph: ')
    df = pd.DataFrame(eventList)
    df['size']=9 # set default marker size
    # adjust y values since tkinter plots starting at the top left
    df['y'] = df['y'].apply(lambda x: 500 - x if x != 0 else x)
    df['y2'] = df['y2'].apply(lambda x: 500 - x if x != 0 else x)

    annotations_list = []

    for index, row in df.iterrows():
        # print(row)
        test = row['event_type']
        if test in ('Cross', 'Pass', 'SetPlay', 'Corner'):
            arrow = go.layout.Annotation(dict(
                x=row['x2'],
                y=row['y2'],
                xref="x", yref="y",
                text="",
                showarrow=True,
                axref="x", ayref='y',
                ax=row['x'],
                ay=row['y'],
                arrowhead=2,
                arrowwidth=1.5,
                arrowcolor='gray',
                opacity=0.7,
                startstandoff=4
            )
            )
            annotations_list.append(arrow)

    color_discrete_map = {'Shot': 'red', 'Cross': '#0B2B5A', 'Assist': 'deepskyblue', 'Pass': 'lightgray',
                          'None': 'lightgray'}

    fig = px.scatter(df, x='x', y='y',color='event_type', size='size',
                     hover_name="event_type",
                     range_x=[0, 690], range_y=[0, 520], size_max=9,
                     width=690, height=520, color_discrete_map=color_discrete_map, opacity=0.7,
                     hover_data={'player':True, 'teamid':True, 'event_type':True,'x':False, 'y':False, 'matchid':False,
                                 'phase_type':False, 'size':False})

    fig.update_layout(
        annotations=annotations_list, )

    # Add halos
    fig.update_traces(marker=dict(
        line=dict(width=1,
                  color='darkgray')),
        selector=dict(mode='markers'))

    # Remove side color scale and hide zero and gridlines
    fig.update_layout(
        coloraxis_showscale=False,
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False)
    )

    # Format the title header to be centered
    '''fig.update_layout(
        title={
            'text': title,
            'y': 1,
            'x': 0.52,
            'xanchor': 'center',
            'yanchor': 'top'})'''

    # Blank out legend title since we don't really need a title. It's self explanatory
    fig.update_layout(legend_title_text='')

    # Position the legend horizontally on top
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.1,  # Negative number puts the legend at the bottom
        xanchor="right",
        x=1
    ))

    # Disable axis ticks and labels
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='')
    image_file = 'Pitch.png'
    # image_file = 'WhitePitch.png'

    from PIL import Image

    img = Image.open(image_file)

    fig.add_layout_image(
        dict(
            source=img,
            xref="x",
            yref="y",
            x=0,
            y=520,
            sizex=690,
            sizey=520,
            sizing="stretch",
            opacity=0.5,
            layer="below")
    )

    # Sets background to white vs grey
    fig.update_layout(template='plotly_dark',
                      xaxis=dict(
                          showgrid=False,
                          showticklabels=False),
                      plot_bgcolor='black',
                      #paper_bgcolor='rgba(0, 0, 0, 0)'
                      )

    fig.update_layout(
        font_family="Arial",
        title_font_family="Arial"
    )
    #plt.show()
    fig.show()

print('Finished!!!')
