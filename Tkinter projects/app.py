from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
T= Tk()
T.title("Image loading")
T.geometry("500x500")
image1 = Image.open("i6.jpeg")
image2 = ImageTk.PhotoImage(image1)
L1 = Label(T, image=image2, height=300, width=300)
L1.place(x=50, y=50)
L2 = Label(T, text="This is an Image in Tkinter")
L2.place(x=40, y=340)
T1=Entry(T)
T1.place(x=40, y=370)
def f1():
    messagebox.showwarning("Alert", "Virus Threat")
    top=Toplevel()#new window
    top.geometry("300x300")
    top.title("Another window")
    L=Label(top, text="Hello")
    L.pack()
    top.mainloop()
B=Button(T, text="Scan for Virus", command=f1)
B.place(x=50, y=480)
T.mainloop()

#After class project Try with rock paper siccors