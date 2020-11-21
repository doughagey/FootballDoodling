# FootballDoodling

## Overview

* `FootballDoodling` helps you to manually graph match events and export the results in csv format

* Below are some tips and examples on how to use `FootballDoodling` to draw event graphs
  
## Usage

Running the script is quite simple and can be done via any IDE or other preferred Python working environment. Upon running the script the user will be asked a handful of
questions regarding the match, player/team, game phase and event type. In the current version you must run the script separately for each event type that you wish to 
graph (once for shots, once for passes, etc.). As long as you elect not to start with a fresh csv file it will append all of
the events to the same output file and you can use this file to plot the events in the graphical tool of your choice, or simply store the data
in a file or database for later use. 

In the current version you must double-click for single marker events such as shot locations and single click for all events
which have a different starting point and endpoint. Each time you complete an event marker it will change from blue to orange in colour. 
If a marker has not yet changed colour you can click outside of the pitch in the white space and it will change. However, I advise not to click outside of the pitch
area until you are finished with all your markers. Else it will cause problems. Also, in this version please do NOT mix single-click and double-click event types. It will 
not handle it properly currenlty.

## Examples

Here is an example of the interface showing crosses:

![Screenshot](Example.png)


Here is an example of the interface showing shots:

![Screenshot](Example2.png)
