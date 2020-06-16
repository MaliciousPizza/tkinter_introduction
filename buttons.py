import tkinter as tk

root = tk.Tk()

# create a function to do something when the button is clicked
# function just creates a label that will say the button has been clicked
def myClick():
    myLabel = tk.Label(root,text='button has been clicked')
    myLabel.pack()

# Buttons are just another widget
myButton = tk.Button(root, text='click me')
myButton.pack()

# can change the state of buttons to make them disabled.. et al
myButton2 = tk.Button(root, text='Disabled Button', state='disabled')
myButton2.pack()

# can add padding to the buttons using padx and pady
myButton3 = tk.Button(root, text='button with padding', pady=50, padx=15)
myButton3.pack()

# buttons that can run functions, the functions should not have the parentheses
myButton4 = tk.Button(root, text='click me to run command', command=myClick)
myButton4.pack()

# change the colors of the buttons
# make the background a different color
myButton5 = tk.Button(root, text='red button', bg="red")
myButton5.pack()

# make the letters in the button colored.
myButton6 = tk.Button(root, text='red letters', fg="red")
myButton6.pack()


root.mainloop()