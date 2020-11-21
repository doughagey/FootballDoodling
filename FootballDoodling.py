import matplotlib.pyplot as plt
import pandas as pd
import os
from pathlib import Path
from matplotlib.widgets import TextBox
import matplotlib.gridspec as gridspec

def graphDrawing(markList):
    if len(markList) == 2:
        plt.plot(markList[0], markList[1], 'o', color='orange')
    elif len(markList) == 4:
        pass
    else:
        print('Not enough data to plot')

def onclick(event):
    xcoords.append(event.xdata)
    ycoords.append(event.ydata)

    # Update plotted coordinates
    graph_2.set_xdata(xcoords)
    graph_2.set_ydata(ycoords)

    # Refresh the plot
    fig.canvas.draw()

    if event.dblclick:
        row = [xcoords[0], ycoords[0]]
        graphDrawing(row)
        list_of_rows.append(row)
        xcoords.clear()
        ycoords.clear()

    elif len(xcoords) == 2:
        row = [xcoords[0], ycoords[0], xcoords[1], ycoords[1]]
        graphDrawing(row)
        list_of_rows.append(row)
        xcoords.clear()
        ycoords.clear()


# Get info up fron we we don't have to later
playerid = input('Enter player name or ID: ')
matchid= input('Please enter match name or ID: ')
event_type = input('Please enter event type (Shot, Cross, Pass, SetPlay): ')
teamid = input('Please enter team name or ID: ')
phase_type = input('Please enter game phase type (return for OpenPlay): ')

if len(phase_type)<3:
    phase_type = 'OpenPlay'

fig,ax = plt.subplots()
plt.ylim(-3650, 3650)
plt.xlim(-5300, 5300)

filename = os.path.join(os.getcwd(),'Pitch.png')
im = plt.imread(filename)

graph_2, = ax.plot([], marker='.')

# Keep track of x/y coordinates
xcoords = []
ycoords = []
list_of_rows = []

x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.imshow(im, extent=[x0, x1, y0, y1], aspect='auto', zorder=0)
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show(block=True)

print(list_of_rows)

# Create empty dataframe to hold values once clicked on image
if event_type in ['Pass','Cross', 'SetPlay']:
    column_names = ['location_x', 'location_y', 'target_x', 'target_y']
elif event_type == 'Shot':
    column_names = ['location_x', 'location_y']
df = pd.DataFrame(columns = column_names)

for coordinate in list_of_rows:
    series = pd.Series(coordinate, index = df.columns)
    df = df.append(series, ignore_index=True)

df['player_id'] = playerid
df['match_id'] = matchid
df['event_name'] = event_type
df['team_id'] = teamid
df['phase_type'] = phase_type
print(df)

try:
    df.to_csv(r'FootballDoodling.csv', index = False, header=True)
except Exception as e:
    print(e)
