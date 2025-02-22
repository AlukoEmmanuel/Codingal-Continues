

from tkinter import *
T=Tk ()
T.title("sample window")
T.geometry("300x300")
L1=Label(text="Enter your name : ",bg="black" ,fg="white")
E1=Entry(fg="yellow" , bg="blue" , width=50)
L2=Label (text="Enter your Age : ",bg="black" ,fg="white")
E2=Entry(fg="yellow" , bg="blue" , width=50)
B=Button(text="Click Me",bg="red",fg="green")
L1.pack()
E1.pack()
L2.pack()
E2.pack()
B.pack()

F=Frame(master=T, relief=RAISED,borderwidth=5)
F.pack()
L3=Label (master=F, text="In Frame")
L3.pack()

T=Text(fg="pink" , bg="blue")
T.pack()
