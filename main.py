BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

current_card = {}
data_dict = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(question, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(question, text=current_card["English"], fill="white")


def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
back_img = PhotoImage(file="images/card_back.png")
front_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_img)

language = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
question = canvas.create_text(400, 283, text="SubTitle", font=("Arial", 60, "italic"))
canvas.grid(column=0, row=0, columnspan=2)


wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()

