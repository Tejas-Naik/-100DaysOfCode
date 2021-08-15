from tkinter import *
import pandas
import random

# ------------------------Next card---------------------

current_card = {}
to_learn = {}

try:
    # words_to_learn.csv
    data = pandas.read_csv('data/french_words.csv')
except FileNotFoundError:
    original_data = pandas.read_csv(
        'data/french_words.csv')    # french_words.csv
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')  # French
    canvas.itemconfig(
        card_word, text=current_card['French'], fill='black')  # French
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, flip_card)

# def next_eng_card():
#     word_to_learn = current_card['English']
#     canvas.itemconfig(card_title, text='English')
#     canvas.itemconfig(card_word, text=word_to_learn)
#     card_back_image = PhotoImage('images/card_back.png')
#     canvas.create_image(400, 263, image=card_back_image)

def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# ---------------------------UI-------------------------
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# flipping a card
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images\card_front.png")
card_back_image = PhotoImage('images/card_back.png')
# Front image
# Background colour and getting rid of the border
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# Title text
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 265, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Wrong Button
cross_image = PhotoImage(file='images\wrong.png')
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

# Right Button
check_image = PhotoImage(file='images/right.png')
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# we are calling the next_card to get the first new card
next_card()

window.mainloop()
