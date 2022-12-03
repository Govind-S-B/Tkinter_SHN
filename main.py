from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.geometry("1000x600")

img1=ImageTk.PhotoImage(Image.open("./src/color1.jpg"))
img2=ImageTk.PhotoImage(Image.open("./src/color2.jpg"))
img3=ImageTk.PhotoImage(Image.open("./src/color3.jpg"))
img4=ImageTk.PhotoImage(Image.open("./src/color4.jpg"))
img5=ImageTk.PhotoImage(Image.open("./src/color5.jpg"))

l=Label(root,font="bold")
l.pack()

x=1

def move():
    global x
    if x==6:
        x=1
    if x==1:
        l.config(image=img1)
    elif x==2:
        l.config(image=img2)
    elif x==3:
        l.config(image=img3)
    elif x==4:
        l.config(image=img4)
    elif x==5:
        l.config(image=img5)

    x+=1
    root.after(33, move)

move()
mainloop()