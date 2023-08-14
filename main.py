import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 1

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN  * 60
    while reps <= 8:
        if reps % 8 == 0:
            countdown(long_break_sec)
            reps += 1
        elif reps % 2 == 0:
            countdown(short_break_sec)
            reps += 1
        else:
            countdown(work_sec)
            reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")
    if count > 0:
        window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Creating canvas in the window
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Creating the image to put in the canvas
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)   # Placing the image approx at the center of the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))    # Place the text in the center of the tomato
canvas.grid(column=1, row=1)



# Timer Label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

# Checkbox Label
checkbox_label = Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"))
checkbox_label.grid(column=1, row=3)


# Start button
start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)


# Reset button
reset_button = Button(text='Reset')
reset_button.grid(column=2, row=2)



window.mainloop()
