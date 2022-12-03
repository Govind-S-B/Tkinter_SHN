from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.geometry("1000x600")

seed_img = Image.open("./src/test.jpg")
l=Label(root,font="bold")
l.pack()

x=1

show_img = seed_img.rotate(0.1*x)
img1=ImageTk.PhotoImage(show_img)

def move():
    global x
    global seed_img
    global img1

    show_img = seed_img.rotate(1*x)
    img1=ImageTk.PhotoImage(show_img)
    
    l.config(image=img1)

    x+=1
    root.after(1, move)

move()
mainloop()