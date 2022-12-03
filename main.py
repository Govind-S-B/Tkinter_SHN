from tkinter import *
from PIL import Image,ImageTk

root=Tk()

root.geometry("1000x600")
root.minsize(1000,600)
root.maxsize(1000,600) # based on crop image size

l=Label(root)
l.pack()
frame_count=1

rotate_angle_per_frame = 1
fps  = 60

seed_img = Image.open("./src/seed_image_3.png") # seed image is just a pregenerated mesh gradient with blur and noise added

# TIPS TO GENERERATE SEED IMAGES
# https://meshgradient.com generate mesh gradient from website
# https://www.img2go.com/crop-image crop to 1500x1500 and compression to 40%

crop_img = seed_img.crop((250, 250, 1250, 1250)) # configured for 1500x1500 seed

final_frame=ImageTk.PhotoImage(crop_img)

def move():
    global frame_count
    global seed_img
    global intermediate_img
    global crop_img
    global final_frame

    intermediate_img = seed_img.rotate(rotate_angle_per_frame*frame_count)
    crop_img = intermediate_img.crop((250, 250, 1250, 1250))
    final_frame=ImageTk.PhotoImage(crop_img)
    
    l.config(image=final_frame)

    frame_count+=1
    root.after(int(1000/fps), move)

move()
mainloop()