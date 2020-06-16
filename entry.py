import tkinter as tk

root = tk.Tk()

# create an entry box or text box
entryBox = tk.Entry()
# give it a placeholder
entryBox.insert(0,'This is a placeholder')
entryBox.pack()

# create a funciton that will retrieve what is in the entry box and return it to the label. 
def myClick():
    # the .get method will get the information from the entrybox and store it as a variable. 
    entryText = entryBox.get()
    myLabel = tk.Label(root,text=entryText)
    myLabel.pack()


# button to retirev text
button = tk.Button(root,text='retrieve text btn',command=myClick)
button.pack()

#change the width of the box
entryBox2 = tk.Entry(root,width=50)
entryBox2.pack()

# change the color of the entry box
# changes the background color
entryBox3 = tk.Entry(root,bg="blue")
entryBox3.pack()

#changes the color of the letters
entryBox4 = tk.Entry(root,fg="blue")
entryBox4.pack()

#changes the border width
entryBox5 = tk.Entry(root,borderwidth=5)
entryBox5.pack()


root.mainloop()