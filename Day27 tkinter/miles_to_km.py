import tkinter

window = tkinter.Tk()
window.title('Miles to Kilometer')
window.minsize(width=250, height=150)
window.config(padx=30, pady=30)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

equal_label = tkinter.Label(text='is equal to')
equal_label.grid(column=0, row=1)

miles_label = tkinter.Label(text='Miles')
miles_label.grid(column=2, row=0)

def result_label():
    pass


result_label = tkinter.Label(text='')
result_label.grid(column=1, row=1)

result_extention_label = tkinter.Label(text='Kms')
result_extention_label.grid(column=2, row=1)


def calculate_kms():
    output = int(input.get()) * 1.6
    output = round(output, 2)
    result_label.config(text=output)


calculate_button = tkinter.Button(text='Calculate', command=calculate_kms)
calculate_button.grid(column=1, row=2)

window.mainloop()
