from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)


# Creating canvas in the window
canvas = Canvas(width=200, height=224)

# Creating the image to put in the canvas
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_image)   # Placing the image approx at the center of the canvas
canvas.create_text(103, 130, text="00:00", )
canvas.pack()


window.mainloop()
