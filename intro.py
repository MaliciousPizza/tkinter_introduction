import tkinter as tk

#first thing you create is the root widget
root = tk.Tk()

# to create anything in tkinter you have to create it then set it. 
# creating a label widget
myLabel = tk.Label(root, text="hello, world!")
# making it show up on the screen
myLabel.pack()

# event loop to ensure everything will show up.
root.mainloop()