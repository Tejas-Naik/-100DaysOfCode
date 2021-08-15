from tkinter import *

window = Tk()       # creating the window object
window.title('my first GUI program')
window.minsize(width=600, height=500)

# label 
# adding text to the middle of the window
my_label = Label(text='I am a Label', font=('Arial', 24, 'bold'))
# my_label.pack()  #side='left')
my_label.grid(column=0, row=0)

# Updating the component of Label
my_label['text'] = "New Text"
# my_label.config(text="New Text at Label 2")
# my_label.config(text="New Text at Label 2", font=('monoscope', 24, 'italic'))


def got_clicked():
    print("I got clicked!")
    # my_label['text'] = "Button Got Clicked!"
    my_label.config(text=input.get())


# creating Button
button = Button(text='Click me', command=got_clicked)
# button.pack()
button.grid(column=1, row=1)

button = Button(text='Click me', command=got_clicked)
# button.pack()
button.grid(column=2, row=0)

# Entry/Input
input = Entry(width=20)
# input.pack()
input.grid(row=4, column=3)

# using the Pack manager by using the Pack manager you can give the X and Y positions for the widgets
## input.place(x=0, y=0)

# Final manager is Grid which is very useful you specify the columns and rows
## my_label.grid(column=0, row=0)
## button.grid(column=1, row=1)
## my_input.grid(column=2, row=2)


# if you want to add padding around the widgets
# {name_of_label}.config(padx=20, pady=20) 
window.mainloop()           # keeping the window until we close it
