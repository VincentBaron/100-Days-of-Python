from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas_img.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    tick_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        title_label.config(text="Long Break", fg="orange")
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title_label.config(text="Short Break", fg="green")
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text="Work", fg="purple")
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas_img.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        tick_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
canvas_img = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas_img.create_image(100, 112, image=image)
timer_text = canvas_img.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


button_start = Button(text="Start", command=start_timer)
button_reset = Button(text="Reset", command=reset_timer)
tick_label = Label(bg=YELLOW, foreground="green", font=(FONT_NAME, 35, "bold"))
title_label = Label(text="Timer", bg=YELLOW, fg="blue", font=(FONT_NAME, 35, "bold"))

canvas_img.grid(column=1, row=1)
button_start.grid(column=0, row=2)
button_reset.grid(column=2, row=2)
tick_label.grid(column=1, row=3)
title_label.grid(column=1, row=0)

window.mainloop()