from tkinter import *
# from tkinter.ttk import *
import tkinter as tk
import sqlite3 as sq
from PIL import Image, ImageFont, ImageDraw, ImageTk

root = Tk()
root.geometry("1000x600")
root.minsize(600, 400)

canvas = Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)


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



x = 1
for i in result:

    bg = Image.open("./src." + i[2] + ".png")
    draw = ImageDraw.Draw(bg)
    date_ = i[0].split("-")
    date = date_[2]+"-"+date_[1]+"-"+date_[0]
    draw.text((70, 30), date, fill="black", anchor="ms", font=font1)
    draw.text((50, 60), i[1], fill="white", anchor="ms", font=font2)
    bg.save("./cards." + i[0] + ".png")

    photo = PhotoImage("./cards." + i[0] + ".png")
    Label(canvas, image=photo).grid(column=x, row=1, sticky=S)

    Label(canvas, text=i[1], bd=5,
          relief='groove').grid(column=x, row=1, sticky=S)
    x += 1
    if x == 3:
        break

mainloop()
