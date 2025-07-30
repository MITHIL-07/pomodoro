import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg="green")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break", fg="red")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Short Break", fg="pink")
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg="green")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg="white")

title_label = tk.Label(text="Timer", fg="green", bg="white", font=("Courier", 35, "bold"))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg="white", highlightthickness=0)
timer_text = canvas.create_text(100, 112, text="00:00", fill="black", font=("Courier", 30, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = tk.Label(fg="green", bg="white", font=("Courier", 20, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
                                                   


