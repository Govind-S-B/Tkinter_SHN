from tkinter import *
import tkinter as tk
import sqlite3 as sq
from PIL import Image, ImageFont, ImageDraw, ImageTk
import os
import textwrap

root = Tk()
root.geometry("1000x600")
root.minsize(1000, 600)
root.maxsize(1000, 600)


def prevPage(event):
    root.destroy()
    import main


font1 = ImageFont.truetype("./src/Uni Sans Heavy.otf", 20)
font2 = ImageFont.truetype("./src/Uni Sans Heavy.otf", 15)
return_img = ImageTk.PhotoImage(Image.open(f"./src/return.png"))

canvas = Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

canvas.create_image(30, 30, image=return_img)
canvas.tag_bind(return_img, "<Button-1>", prevPage)

conn = sq.connect('report.db')
cursor = conn.cursor()
query = """
        SELECT *
        FROM REPORT
        ORDER BY DATE DESC
"""
cursor.execute(query)
result = cursor.fetchall()

font1 = ImageFont.truetype("./src/Uni Sans Heavy.otf", 20)
font2 = ImageFont.truetype("./src/Uni Sans Heavy.otf", 15)

path = "./cards/"
if not os.path.exists(path):
    os.makedirs(path)

column = 1
row = 1
for i in result:

    bg = Image.open("./src/" + i[2] + ".png")
    draw = ImageDraw.Draw(bg)
    date_ = i[0].split("-")
    date = date_[2]+"-"+date_[1]+"-"+date_[0]
    draw.text((75, 30), date, fill="black", anchor="ms", font=font1)
    offset = 60
    for line in textwrap.wrap(i[1], width=15):
        draw.text((80, offset), line, font=font2, fill='white', anchor="ms")
        offset += 18
    bg.save("./cards/" + i[0]+".png")

    photo = PhotoImage(file="./cards/" + i[0]+".png")
    label = Label(canvas, image=photo)
    label.image = photo
    label.grid(column=column, row=row, sticky=S)

    column += 1
    if column > 4:
        row += 1
        column = 1

    os.remove("./cards/" + i[0]+".png")

mainloop()
