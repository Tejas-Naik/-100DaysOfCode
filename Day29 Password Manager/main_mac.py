from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)  #, bg="#e2979c")
image_logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image_logo)
canvas.grid(column=1, row=0)
# Website Text
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
# Email/Username Text
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
# Password Label
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)


# Website Input
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
# Email/Username Input
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
# Password Input
password_input = Entry(width=21)
password_input.grid(column=1, row=3)


# Buttons
pass_button = Button(text='Generate Password')
pass_button.grid(column=2, row=3)
# add button
add_button = Button(text='Add', width=36)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
