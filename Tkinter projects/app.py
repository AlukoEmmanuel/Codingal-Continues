from tkinter import *
from PIL import Image, ImageTk
T= Tk()
T.title("Image loading")
T.geometry("500x500")
image1 = Image.open("i6.jpeg")
image2 = ImageTk.PhotoImage(image1)
L1 = Label(T, image=image2, height=400, width=300)
L1.place(x=50, y=50)
L2 = Label(T, text="This is an Image in Tkinter")
L2.place(x=40, y=440)
T=Entry(T)
T.place(x=40, y=500)
T.mainloop()