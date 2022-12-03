from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.geometry("1000x600")
root.minsize(1000,600)
root.maxsize(1000,600)

l=Label(root,font="bold")
l.pack()

x=1

seed_img = Image.open("./src/test.jpg")
seed_img = seed_img.rotate(0.1)
crop_img = seed_img #.crop((500,500,500,500))
img1=ImageTk.PhotoImage(crop_img)

def move():
    global x
    global seed_img
    global crop_img
    global img1

    seed_img = seed_img.rotate(0.1*x)
    crop_img = seed_img #.crop((500,500,500,500))
    img1=ImageTk.PhotoImage(crop_img)

    
    l.config(image=img1)

    x+=1
    root.after(1, move)

move()
mainloop()