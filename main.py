from tkinter import *
from PIL import Image,ImageTk
import random
from tkinter import ttk
import tkinter.font as tkFont
import _sqlite3 as sq
from datetime import date

conn = sq.connect("report.db")
stmt = "SELECT name FROM sqlite_master WHERE type='table' AND name='REPORT';"
cursor = conn.execute(stmt)
result = cursor.fetchone()
if result:
    pass
else:
    conn.execute('''CREATE TABLE REPORT 
        (DATE          DATE             PRIMARY KEY     NOT NULL,
        DESCRIPTION    CHAR(100)                        NOT NULL,
        MOOD           CHAR(10)                         NOT NULL);''')


root=Tk()
root.title("Mood Tracker")
root.geometry("1000x600")
root.minsize(1000,600)
root.maxsize(1000,600) # based on crop image size
# root.eval('tk::PlaceWindow . center')
qstn_font = tkFont.Font(family="havletica", size=30, weight="bold")

l=Label(root)
l.pack()
frame_count=1

rotate_angle_per_frame = 1
fps = 60

# Button Click Functions
happy_state = 0
def happy_button_clicked(event):
    global happy_state, selected_mood
    print("Button clicked: 1")
    if happy_state == 0:
        happy_state = 1
    else:
        happy_state = 0
    selected_mood = "happy"

confused_state = 0
def confused_button_clicked(event):
    global confused_state, selected_mood
    if confused_state == 0:
        confused_state = 1
    else:
        confused_state = 0
    print("Button clicked: 2")
    selected_mood = "confused"

sad_state = 0
def sad_button_clicked(event):
    global sad_state, selected_mood
    if sad_state == 0:
        sad_state = 1
    else:
        sad_state = 0
    print("Button clicked: 3")
    selected_mood = "sad"

star_state = 0
def star_button_clicked(event):
    global star_state, selected_mood
    if star_state == 0:
        star_state = 1
    else:
        star_state = 0
    print("Button clicked: 4")
    selected_mood = "star"

angry_state = 0
def angry_button_clicked(event):
    global angry_state, selected_mood
    if angry_state == 0:
        angry_state = 1
    else:
        angry_state = 0
    print("Button clicked: 5")
    selected_mood = "angry"

def submit():
    global description, selected_mood
    description = e1.get()
    print(selected_mood)
    print(description)
    today = date.today()
    print(today)
    conn.execute(f"INSERT INTO REPORT VALUES ('{today}', '{description}', '{selected_mood}');")
    conn.commit()

def cal_icon_click(event):
    root.destroy()
    import page2test

## to put inside 2nd page py file
# def prevPage():
#     root.destroy()
#     import page1

num = random.randint(1,3)
print(num)
seed_img = Image.open(f"./src/seed_image_{num}.png") # seed image is just a pregenerated mesh gradient with blur and noise added

# TIPS TO GENERERATE SEED IMAGES
# https://meshgradient.com generate mesh gradient from website
# https://www.img2go.com/crop-image crop to 1500x1500 and compression to 40%

crop_img = seed_img.crop((250, 250, 1250, 1250)) # configured for 1500x1500 seed

final_frame=ImageTk.PhotoImage(crop_img)

# --------------------------------------------------------------------------
# frame = Frame(root, width=800, height=600, background="#3f3f3f", padx=30, pady=50)
# frame.pack()
# frame.place(anchor='center', relx=0.5, rely=0.25)

# label2 = Label(frame, text="How was your day?",background="#3f3f3f", font="havletica 20", foreground="white", padx=20, pady=20)
# label2.pack()

# submit_button = Button(frame, text="Submit", padx=40, pady=8, font="havletica 11", background="#255EC9", foreground="white")

# root.wm_attributes('-transparentcolor', '#3f3f3f')

# Emoji images
happy_emoji = ImageTk.PhotoImage(Image.open(f"./src/happy.png"))
happy_emoji_big = ImageTk.PhotoImage(Image.open(f"./src/happy_big.png"))
confused_emoji = ImageTk.PhotoImage(Image.open(f"./src/confused.png"))
confused_emoji_big = ImageTk.PhotoImage(Image.open(f"./src/confused_big.png"))
sad_emoji = ImageTk.PhotoImage(Image.open(f"./src/sad.png"))
sad_emoji_big = ImageTk.PhotoImage(Image.open(f"./src/sad_big.png"))
star_emoji = ImageTk.PhotoImage(Image.open(f"./src/star.png"))
star_emoji_big = ImageTk.PhotoImage(Image.open(f"./src/star_big.png"))
angry_emoji = ImageTk.PhotoImage(Image.open(f"./src/angry.png"))
angry_emoji_big = ImageTk.PhotoImage(Image.open(f"./src/angry_big.png"))

# Icons
calendar_icon = ImageTk.PhotoImage(Image.open(f"./src/calendar.png"))

canvas = Canvas(root, width=1000, height=700)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=final_frame, anchor="nw")
canvas.create_text(400, 300, text="How was your day?", fill="white")

# submit_button.pack()
#---------------------------------------------------------------------------

def move():
    global frame_count, seed_img, intermediate_img, crop_img, final_frame, happy_button, confused_button, calendar_icon
    global sad_button, angry_button, star_button, happy_state, sad_state, star_state, confused_state, angry_state, selected_mood

    intermediate_img = seed_img.rotate(rotate_angle_per_frame*frame_count)
    crop_img = intermediate_img.crop((250, 250, 1250, 1250))
    final_frame=ImageTk.PhotoImage(crop_img)

    canvas.create_image(0, 0, image=final_frame, anchor="nw")
    canvas.create_text(505, 150, text="How was your day ?", font=qstn_font, fill="white")

    # Emoji Buttons
    left_mar = 350
    if happy_state == 0:
        happy_button = canvas.create_image(left_mar, 225, image=happy_emoji)
    else:
        happy_button = canvas.create_image(left_mar, 225, image=happy_emoji_big)

        # canvas.delete(star_button)
        # canvas.delete(sad_button)
        # canvas.delete(confused_button)
        # canvas.delete(angry_button)

        # star_button = canvas.create_image(left_mar+75, 225, image=star_emoji)
        # sad_button = canvas.create_image(left_mar+150, 225, image=sad_emoji)
        # confused_button = canvas.create_image(left_mar+225, 225, image=confused_emoji)
        # angry_button = canvas.create_image(left_mar+300, 225, image=angry_emoji)

        # star_state = 0
        # sad_state = 0
        # confused_state = 0
        # angry_state = 0
    canvas.tag_bind(happy_button, "<Button-1>", happy_button_clicked)

    if star_state == 0:
        star_button = canvas.create_image(left_mar+75, 225, image=star_emoji)
    else:
        star_button = canvas.create_image(left_mar+75, 225, image=star_emoji_big)

        # canvas.delete(happy_button)
        # canvas.delete(sad_button)
        # canvas.delete(confused_button)
        # canvas.delete(angry_button)

        # sad_button = canvas.create_image(left_mar+150, 225, image=sad_emoji)
        # confused_button = canvas.create_image(left_mar+225, 225, image=confused_emoji)
        # angry_button = canvas.create_image(left_mar+300, 225, image=angry_emoji)
        # happy_button = canvas.create_image(left_mar, 225, image=happy_emoji)
        # angry_state = 0
        # sad_state = 0
        # confused_state = 0
        # happy_state = 0
    canvas.tag_bind(star_button, "<Button-1>", star_button_clicked)

    if sad_state == 0:
        sad_button = canvas.create_image(left_mar+150, 225, image=sad_emoji)
    else:
        sad_button = canvas.create_image(left_mar+150, 225, image=sad_emoji_big)

        # canvas.delete(star_button)
        # canvas.delete(happy_button)
        # canvas.delete(confused_button)
        # canvas.delete(angry_button)

        # happy_button = canvas.create_image(left_mar, 225, image=happy_emoji)
        # star_button = canvas.create_image(left_mar+75, 225, image=star_emoji)
        # confused_button = canvas.create_image(left_mar+225, 225, image=confused_emoji)
        # angry_button = canvas.create_image(left_mar+300, 225, image=angry_emoji)
        # star_state = 0
        # angry_state = 0
        # confused_state = 0
        # happy_state = 0
    canvas.tag_bind(sad_button, "<Button-1>", sad_button_clicked)

    if confused_state == 0:
        confused_button = canvas.create_image(left_mar+225, 225, image=confused_emoji)
    else:
        confused_button = canvas.create_image(left_mar+225, 225, image=confused_emoji_big)

        # canvas.delete(star_button)
        # canvas.delete(sad_button)
        # canvas.delete(happy_button)
        # canvas.delete(angry_button)
        
        # happy_button = canvas.create_image(left_mar, 225, image=happy_emoji)
        # star_button = canvas.create_image(left_mar+75, 225, image=star_emoji)
        # sad_button = canvas.create_image(left_mar+150, 225, image=sad_emoji)
        # angry_button = canvas.create_image(left_mar+300, 225, image=angry_emoji)
        # star_state = 0
        # sad_state = 0
        # angry_state = 0
        # happy_state = 0
    canvas.tag_bind(confused_button, "<Button-1>", confused_button_clicked)

    if angry_state == 0:
        angry_button = canvas.create_image(left_mar+300, 225, image=angry_emoji)
    else:
        angry_button = canvas.create_image(left_mar+300, 225, image=angry_emoji_big)

        # canvas.delete(star_button)
        # canvas.delete(sad_button)
        # canvas.delete(confused_button)
        # canvas.delete(happy_button)

        # happy_button = canvas.create_image(left_mar, 225, image=happy_emoji)
        # star_button = canvas.create_image(left_mar+75, 225, image=star_emoji)
        # sad_button = canvas.create_image(left_mar+150, 225, image=sad_emoji)
        # confused_button = canvas.create_image(left_mar+225, 225, image=confused_emoji)

        # star_state =0
        # sad_state = 0
        # confused_state = 0
        # happy_state = 0
    canvas.tag_bind(angry_button, "<Button-1>", angry_button_clicked)
    
    cal_button = canvas.create_image(40, 40, image=calendar_icon)
    canvas.tag_bind(cal_button, "<Button-1>", cal_icon_click)
    # submit_button = canvas.create_text(550, 350, text="Submit", fill="green",)

    

    frame_count+=1
    root.after(int(1000/fps), move)

string = StringVar()
string.set('Enter input')
e1 = Entry(canvas, background="white", borderwidth=3, textvariable=string, width=40, bd=1)
canvas.create_window(500, 280, window=e1)

# Create style Object
style = ttk.Style()
 
style.configure('TButton', font = ('calibri', 20, 'bold'), borderwidth = '4')
style.map('TButton', foreground = [('active', '!disabled', 'green')], background = [('active', 'black')])

btn = Button(root, text='Submit', width=10, height=1, font="havletica 11", background="#255EC9", foreground="white" ,command=submit)
btn.place(x=450, y=350)
# btn.bind("<Button-1>", submit)

# cal_button = Button(root, image=calendar_icon, command=cal_icon_click)
# cal_button.place(x=30, y=30)
# cal_button.bind()


# btn.pack()


move()
mainloop()