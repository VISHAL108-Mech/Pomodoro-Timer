"""Pomodoro Timer Application using Tkinter."""

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
LONG_BREAK_MIN = 10
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Resets the timer, clears the countdown, and resets the session count."""
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Starts the timer and manages work/break sessions based on the number of 
    repetitions."""
    global REPS
    REPS += 1
    work_session = WORK_MIN * 60
    short_break_session = SHORT_BREAK_MIN * 60
    long_break_session = LONG_BREAK_MIN * 60

    if REPS % 2 != 0:
        count_down(work_session)
        timer_label.config(
            text="Focus", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold")
        )
    elif REPS % 8 == 0:
        count_down(long_break_session)
        timer_label.config(
            text="Long Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 20, "bold")
        )
    else:
        count_down(short_break_session)
        timer_label.config(
            text="Short Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 20, "bold")
        )


# ---------------------------- COUNTDOWN MECHANISM --------------------------- #
def count_down(count):
    """Updates the countdown timer every second and manages the transition
      between work and break sessions."""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            marks += "✔"
        tick_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
"""Sets up the user interface for the Pomodoro timer application."""
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=2, row=2)

# Labels
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=2, row=1)

tick_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
tick_label.grid(column=2, row=4)

# Buttons
start_button = Button(command=start_timer)
start_button.config(text="Start", bg=YELLOW, font=(FONT_NAME, 10, "bold"))
start_button.grid(column=1, row=3)

reset_button = Button(command=reset_timer)
reset_button.config(text="Reset", bg=YELLOW, font=(FONT_NAME, 10, "bold"))
reset_button.grid(column=3, row=3)

window.mainloop()
