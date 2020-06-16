import tkinter as tk
 
root = tk.Tk()
# give the calculator app a title
root.title('Simple Calculator app')

# create an entry box that will take the input of the files. 
e = tk.Entry(root, width=35,borderwidth=5)
# grid needs columnspan to ensure that it is the same length as the buttons across. 
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

# create a function to add the button
def btn_click(number):
    #inserts the number clicked
    #create a variable to append the numbers on
    current = e.get()
    e.delete(0, 'end')
    e.insert(0,str(current) + str(number))

def btn_clear():
    e.delete(0, 'end')

def btn_add():
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    e.delete(0, 'end')

def btn_equal():
    second_number = e.get()
    e.delete(0, 'end')
    e.insert(0, f_num + int(second_number))

# create the buttons for the numbers
btn_1 = tk.Button(root,text=1,padx=40,pady=20,command=lambda: btn_click(1))
btn_2 = tk.Button(root,text=2,padx=40,pady=20,command=lambda: btn_click(2))
btn_3 = tk.Button(root,text=3,padx=40,pady=20,command=lambda: btn_click(3))
btn_4 = tk.Button(root,text=4,padx=40,pady=20,command=lambda: btn_click(4))
btn_5 = tk.Button(root,text=5,padx=40,pady=20,command=lambda: btn_click(5))
btn_6 = tk.Button(root,text=6,padx=40,pady=20,command=lambda: btn_click(6))
btn_7 = tk.Button(root,text=7,padx=40,pady=20,command=lambda: btn_click(7))
btn_8 = tk.Button(root,text=8,padx=40,pady=20,command=lambda: btn_click(8))
btn_9 = tk.Button(root,text=9,padx=40,pady=20,command=lambda: btn_click(9))
btn_0 = tk.Button(root,text=0,padx=40,pady=20,command=lambda: btn_click(0))
btn_dec = tk.Button(root,text=".",padx=39,pady=20,command=lambda: btn_click("."))
btn_addition = tk.Button(root,text="+",padx=39,pady=20,command=btn_add)
btn_sub = tk.Button(root,text="-",padx=39,pady=20,command=lambda: btn_click("-"))
btn_clear = tk.Button(root,text="Clear",pady=20,width=40,command=btn_clear)
btn_posneg = tk.Button(root,text="+-",padx=36.49999999999999644728,pady=20,command=lambda: btn_click())
btn_div = tk.Button(root,text="/",padx=39,pady=20,command=lambda: btn_click("/"))
btn_mult = tk.Button(root,text="*",padx=39,pady=20,command=lambda: btn_click("*"))
btn_equal = tk.Button(root,text="=",padx=39,pady=20,command=btn_equal)

# add all of the buttons to the gui using grid
# top row
btn_clear.grid(row=1,column=0,columnspan=3)
btn_div.grid(row=1,column=3)

# second row
btn_7.grid(row=2,column=0)
btn_8.grid(row=2,column=1)
btn_9.grid(row=2,column=2)
btn_mult.grid(row=2,column=3)

# third row
btn_4.grid(row=3,column=0)
btn_5.grid(row=3,column=1)
btn_6.grid(row=3,column=2)
btn_sub.grid(row=3,column=3)

# fourth row
btn_1.grid(row=4,column=0)
btn_2.grid(row=4,column=1)
btn_3.grid(row=4,column=2)
btn_addition.grid(row=4, column=3)

# fifth row
btn_posneg.grid(row=5,column=0)
btn_0.grid(row=5,column=1)
btn_dec.grid(row=5,column=2)
btn_equal.grid(row=5,column=3)



root.mainloop()