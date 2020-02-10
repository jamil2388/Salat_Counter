from tkinter import *

### FUNCTIONS

def my_click1():
    global sample_counter
    print(sample_counter)
    my_label_x1 = Label(root, text="Look, Clicked a Button")
    my_label_x1.grid(row = 4 + sample_counter, column = 0)
    sample_counter += 1
    # my_label_x1.pack()

# GLOBALS

sample_counter = 0

# create the root widget (main window)
root = Tk()

# create a label widget
my_label1 = Label(root, text = "Hello World")
my_label2 = Label(root, text = "Second Text")
my_label3 = Label(root, text = "Third Text")

# create a button widget
my_button1 = Button(root, text = "Button1", padx = 50, pady = 10, command = my_click1, bg = "#95bfa1", fg = "#49614f")
my_button2 = Button(root, text = "Button2", fg = "#49614f")


### PACK (Either Grid or Pack is Allowed)

# my_button1.pack()
# my_button2.pack()

### GRID

# instead of pack, using grid to place the widgets in deliberate positions
my_label1.grid(row = 0, column = 0)
my_label2.grid(row = 1, column = 2)
my_label3.grid(row = 2, column = 6)

# place the buttons
my_button1.grid(row = 1, column = 1)
my_button2.grid(row = 3, column = 1)



# run the main loop (Here it is Root)
root.mainloop()