import tkinter as tk

root = tk.Tk()

myLabel = tk.Label(root,text='Hello, World!')
myLabel2 = tk.Label(root, text= 'Hey this is a new label')

# with grid you have to specify which row and column you would like the widget to be in.
# Columns and rows start with 0. 
myLabel.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

root.mainloop()