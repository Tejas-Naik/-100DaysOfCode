from tkinter import *
import math
import os
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text='Timer')
    checkmark_label.config(text='')
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # count_down(1500)
    global reps

    WORK_SEC = 25 * 60
    SHORT_BREAK_SEC = 5 * 60
    LONG_BREAK_SEC = 20 * 60
    
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_label.config(text='WORK👨‍💻', fg=GREEN)
        count_down(WORK_SEC)
    
    elif reps == 2 or reps == 4 or reps == 6:
        timer_label.config(text='REST😴', fg=PINK)
        count_down(SHORT_BREAK_SEC)
    
    elif reps == 8:
        timer_label.config(text='REST😴😴', fg=RED)
        count_down(LONG_BREAK_SEC)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# countdown Mechanism
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = '00'
    
    if int(count_sec) < 10:
        count_sec = int(count_sec)
        count_sec = f"0{count_sec}"
    
    if count_min == 0 and int(count_sec) == 0:
        reps += 1

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += '✔'
        checkmark_label.config(text=mark)
# we are gonna use Canvas for this 
# highlightthickness will remove the edged
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')            # we have to use PhotoImage to get the photo
canvas.create_image(100, 112, image=tomato_img)       # we have to put the x, y axises 
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Timer text
# canvas.create_text(100, 10, text="Timer", fill=GREEN, font=(FONT_NAME, 35, 'bold'))
timer_label = Label(text="Timer⏲", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))
timer_label.grid(column=1, row=0)

# Start button
start_button = Button(text="Start", width=5, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", width=5, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# checkmark
checkmark_label = Label(font=(FONT_NAME, 25, 'bold'), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=4)



window.mainloop()

# DYNAMIC TYPING
# Dynamic typing is that you can change a variable's type by changing the content
#     a = 5
#     a = "Hello"
