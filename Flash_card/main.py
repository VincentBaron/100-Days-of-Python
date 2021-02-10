from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"


# ----------------------- DATA ------------------------------------

words_list = pandas.read_csv("./data/french_words.csv")
words_dict = words_list.to_dict(orient="records")
#print(words_dict)


def next_card():
    current_card = random.choice(words_dict)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])

# ----------------------- GRAPHICAL INTERFACE ------------------------------------

window = Tk()

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)

front_card = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=front_card)
card_title = canvas.create_text(400, 150, text="Title", font=["Ariel", 40, "italic"])
card_word = canvas.create_text(400, 263, text="Word", font=["Ariel", 60, "bold"])
canvas.grid(row=0, column=0, columnspan=2)

w_button_img = PhotoImage(file="./images/wrong.png")
r_button_img = PhotoImage(file="./images/right.png")
wrong_button = Button(image=w_button_img, highlightthickness=0, command=next_card)
right_button = Button(image=r_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()