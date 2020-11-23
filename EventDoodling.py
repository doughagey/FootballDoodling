import tkinter as tk
from PIL import ImageTk
from PIL import Image as Img
from tkinter import *

def click(e):
    # define start point for line
    coords["x"] = e.x
    coords["y"] = e.y

    # create a line on this point and store it in the list
    lines.append(canvas.create_line(coords["x"],coords["y"],coords["x"],coords["y"],fill='white'))

def drag(e):
    # update the coordinates from the event
    coords["x2"] = e.x
    coords["y2"] = e.y

    # Change the coordinates of the last created line to the new coordinates
    canvas.coords(lines[-1], coords["x"],coords["y"],coords["x2"],coords["y2"])

def actionList():
    playerid = player_input.get()
    teamid = team_input.get()
    eventList.append({'player':playerid,'teamid':teamid})
    eventList[0].update(coords)
    #eventList.append(coords)
    print(eventList)

eventList = []
root = tk.Tk()
width, height = 800, 600

background_image=tk.PhotoImage(file="Pitch2.png")

#
'''image = Img.open('Pitch2.png')
# The (450, 350) is (height, width)
image = image.resize((450, 350), Img.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
my_img = Label(image = my_img)'''
#my_img.pack()
#
root.resizable(width=True, height=True)
root.wm_attributes("-topmost", 1)
canvas = tk.Canvas(root, bg="white", width=690, height=550)

# This is the player textbox
player_input = tk.Entry (root)
canvas.create_window(50, 530, window=player_input, width = 100)

playerLabel = tk.Label(root, text='Player Name/Id:')
playerLabel.config(font=('Arial', 10))
canvas.create_window(40, 500, window=playerLabel)

# This is the team textbox
team_input = tk.Entry (root)
canvas.create_window(160, 530, window=team_input, width = 100)

playerLabel = tk.Label(root, text='Player Name/Id:')
playerLabel.config(font=('Arial', 10))
canvas.create_window(155, 500, window=playerLabel)

# This is the button to submit
submit_button = tk.Button(text='Submit', command=actionList)
canvas.create_window(600, 530, window=submit_button)

# End of regular stuff
canvas.pack(fill=tk.BOTH, expand=1) # Stretch canvas to root window size.
image = canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

coords = {"x":0,"y":0,"x2":0,"y2":0}
# keep a reference to all lines by keeping them in a list
lines = []
canvas.bind("<ButtonPress-1>", click)
canvas.bind("<B1-Motion>", drag)

root.mainloop()
print('Finished!!!')
