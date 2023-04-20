# Python GUI with Tkinter


## Basic - GUI with Tkinter

Tkinter is a Python module used to create simple GUI apps.   

Two ways to import Tkinter :   
- from tkinter import *   => the best way
- import tkinter          => we have to define all the widgets as tkinter.Label , tkinter.Button ...   

Create the window :   
- window = Tk() => Creates a blank windows with close, max and min buttons   
- window.title("My first GUI") => to rename the title of the window
- window.geometry("300x350") => to set the size of the window   

Display the window until you manually close it :  
- window.mainloop()   

Some widgets (Full list on https://docs.python.org/3/library/tkinter.ttk.html#widget) :   
- Button  
- Canvas => used to draw/paint shapes in the window   
- Checkbutton => used to create check buttons in the window. More than one option at a time   
- Entry => used to create input fields in the window. delete(0,end)  
- Frame => used to organise widgets into different areas in the window   
- Label => used to create a single line widget for displaying text or images   
- Menu => used to create menus in the window   

Layout :   
- pack() => easiest way, but not the best. The widget occupies the entire available width
- grid() => to pack widgets into rows and columns. Very handy for forms. row, column, rowspan, columnspan, sticky, ipadx     
- place() => It's used to place the widgets at a specific position you want.   

Organise the layout of widgets with Frames() - the window is also a Frame. For example :
- top_frame = Frame(window) and top_frame.pack()  
- bottom_frame = Frame(window) and ...  
- third_frame = Frame(window) and ...  


Aligning widgets :  
- side=LEFT	align widget to the left side.  
- side=RIGHT align widget to the right side.  
- side=TOP	align widget to the top side.  
- side=BOTTOM	align widget to the bottom side.

For example :   
- button1 = Button(top_frame, text="Button 1", fg="green")   
  button1.pack(side = LEFT)  
creates a button and place it into top_frame container on the left


- def function_name() to define a function
- len(text) to get the size of a string  
- config() allows your code to display/change the text in your Tkinter widgets.  
config(text="") to update Labels and print text onto GUI widgets.  
config(state=DISABLED) to disable a button
- get() to get the data of an entry widget
- exit(0) to terminate/finish this python program and return code 0; meaning no errors

See https://www.tutorialspoint.com/python/tk_button.htm for the widgets' options