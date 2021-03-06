# FootballDoodling

## Overview

* `FootballDoodling` helps you to manually graph match events and export the results in csv format

* Below are some tips and examples on how to use `FootballDoodling` to draw event graphs
  
## Usage
FootballDoodling was meant for those football fans who don't have access to professional event data.
with this tool you can create your own, while you watch a game or afterwards.

Running the script can be done via any IDE or other preferred Python environment. Upon running the script the user will be presented with
a window which includes several textboxes. Here are a few key points when using the tool:
- The only mandatory textbox to fill out is the Event Type textbox. 
- The current version is picky about which Event Types can be entered. Everything is allowed but if you want to plot events which have arrow 
  annotations then those need to be declared first in the annotated_events.txt file (not doing so will cause events to be improperly graphed and stored). 
- Currently the default annotated events are 'Cross', 'Pass', 'SetPlay', and 'Corner'. 
- These annotated events also require the user to single-click and drag (from starting point to endpoint) to create an annotation. 
- All other non-annotated events will be single marker plots and require the user to use a double-click to enter them as a dot/marker on the plot and be 
  recorded properly in the output file.  
- To submit/record any event click on the Submit button. If you make a mistake, just don't click Submit
- Once submit is clicked the last completed event will be recorded
- After the data is graphed you can use the Plotly camera toolbar object to export
  the graph to a .png file
- The exported csv file will get written over each time so rename it if you want to
  keep the data that is there
- You can write up a quick script to imprort the .csv data into a database or use as is
  for your own graphing purposes
  
Have fun!!!

## Examples

Here is an example showing the initial interface:

![Screenshot](Example.png)


Here is an example of the final graph:

![Screenshot](Example2.png)
