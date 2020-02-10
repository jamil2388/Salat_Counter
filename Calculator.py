from tkinter import *

### FUNCTIONS

def my_click1():
    return

def button_click(number):
    # At first Clear the entry field and insert the taken number
    if(entry_field.get() != '0'):
        current_number = str(entry_field.get()) + str(number)
    else:
        current_number = str(number)
    entry_field.delete(0, END)
    entry_field.insert(0, current_number)

def button_click_clear():
    global f_num
    f_num = 0
    entry_field.delete(0, END)
    entry_field.insert(0, 0)


def button_click_operation(o_name):
    global f_num, operation_name

    # depending on this operation name, the operation will be performed later on pressing equal
    operation_name = o_name
    f_num = int(entry_field.get())
    entry_field.delete(0, END)

def button_click_equal():
    global f_num
    if (operation_name == "add"):
        f_num += int(entry_field.get())
    elif (operation_name == "subtract"):
        f_num -= int(entry_field.get())
    elif (operation_name == "multiply"):
        f_num *= int(entry_field.get())
    elif (operation_name == "divide"):
        f_num /= int(entry_field.get())

    # if the operation_name is "none", the last occurring number will be applied
    print_result()

def print_result():
    global f_num
    entry_field.delete(0, END)
    entry_field.insert(0, f_num)
    f_num = 0

# GLOBALS

# stores current Sum
f_num = 0
# depending on this value the respective operator will be applied
operation_name = "none"
sample_counter = 0


### CREATE Widgets

# Root widget (main window)
root = Tk()
root.title("Neo_Genesis")

# Frame widget
button_frame_1 = Frame(root)
button_frame_2 = Frame(root)

# Entry widget
# here width is the absolute width of this widget, it will take on extra space if needed having the other widget space as they were
entry_field = Entry(root, width = 26, bg = "#95bfa1", border = 0)
# entry_field.insert(0, "Enter your Name : ")

# Label widget


# Button widget
# For Button widget Constructor, the padx and pady only expands the inner area of the button
# But in case of Button.grid() function, the same parameter extends the outside area of the button creating more blank spaces
button_1 = Button(root, text = "1", command = lambda : button_click(1), padx = 30, pady = 20)
button_2 = Button(root, text = "2", command = lambda : button_click(2), padx = 30, pady = 20)
button_3 = Button(root, text = "3", command = lambda : button_click(3), padx = 30, pady = 20)
button_4 = Button(root, text = "4", command = lambda : button_click(4), padx = 30, pady = 20)
button_5 = Button(root, text = "5", command = lambda : button_click(5), padx = 30, pady = 20)
button_6 = Button(root, text = "6", command = lambda : button_click(6), padx = 30, pady = 20)
button_7 = Button(root, text = "7", command = lambda : button_click(7), padx = 30, pady = 20)
button_8 = Button(root, text = "8", command = lambda : button_click(8), padx = 30, pady = 20)
button_9 = Button(root, text = "9", command = lambda : button_click(9), padx = 30, pady = 20)
button_0 = Button(root, text = "0", command = lambda : button_click(0), padx = 30, pady = 20)
button_add = Button(root, text = "+", command = lambda : button_click_operation("add"), padx = 29, pady = 21)
button_multiply = Button(root, text = "*", command = lambda : button_click_operation("multiply"), padx = 30, pady = 20)
button_subtract = Button(button_frame_1, text = "-", command = lambda : button_click_operation("subtract"), padx = 50, pady = 21)
button_divide = Button(button_frame_1, text = "/", command = lambda : button_click_operation("divide"), padx = 50, pady = 21)
button_clear = Button(button_frame_2, text = "clear", command = lambda : button_click_clear(), padx = 38, pady = 20)
button_equal = Button(button_frame_2, text = "=", command = lambda : button_click_equal(), padx = 47, pady = 20)



### PACK (Either Grid or Pack is Allowed)

# my_button1.pack()
# my_button2.pack()

### GRID

### PLACE the Widgets

# Frame

button_frame_1.grid(row = 5, column = 0, columnspan = 3)
button_frame_2.grid(row = 6, column = 0, columnspan = 3)


# Entry
entry_field.grid(row = 0, column = 0, columnspan = 3, pady = 3)

# Label


# Button

button_1.grid(row = 1, column = 0)
button_2.grid(row = 1, column = 1)
button_3.grid(row = 1, column = 2)
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_7.grid(row = 3, column = 0)
button_8.grid(row = 3, column = 1)
button_9.grid(row = 3, column = 2)
button_0.grid(row = 4, column = 1)
button_add.grid(row = 4, column = 0)
button_multiply.grid(row = 4, column = 2)
button_subtract.pack(side = "left")
button_divide.pack(side = "left")
button_clear.pack(side = "left")
button_equal.pack(side = "top")


# run the main loop (Here it is Root)
root.mainloop()