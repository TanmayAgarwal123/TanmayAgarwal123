
from tkinter import *
# to initialize the tkinter module we need to create a root widget and this should be the first widget
root = Tk()
# here we are setting the length and width of the screen
root.geometry("500x600")
# adding text with the label widget
Label(text="Enter the no of entry widget you want to create").pack()
# function to create entry widget on calling
def create():
    for x in range((init_val.get())):
        Entry(root).pack(pady=10)
# declaring type of variable for entry widget
init_val = IntVar()
# creating entry widget to take value for no of entry widgets to
# be created
init_ent = Entry(root, textvariable=init_val).pack()
# creating a button to call the create function
Button(text="Create Now", command=create).pack()
# calling root
root.mainloop()