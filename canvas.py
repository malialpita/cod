import tkinter
from tkinter import*
top=Tk()
w=Canvas(top,height=100,width=200)
w.pack()
w.create_rectangle(50,20,150,80,fill="red")
top.mainloop()
