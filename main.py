from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.1
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f'00:00')
    timer_label.config(text="Timer", width=11, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
    check_label.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # count_down(5*60)
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # count_down(work_sec)
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text = 'Long Break', width=11, fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Short Break', width=11, fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text='Work', fg=GREEN, width=11, font=(FONT_NAME, 35, 'bold'))

    # count_down(work_sec)
    # if reps == 0 or reps % 1 == 0 or reps % 2 == 0 or reps % 3 == 0:
    #
    #     count_down(short_break_sec)
    #     reps += 1
    #     print(reps)
    # elif reps % 4 == 0:
    #     # count_down(work_sec)
    #     count_down(long_break_sec)
    #     reps += 1
    #     print(reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = int(count % 60)

    # if count_sec == 0:
    #     count_sec = "00"
    # if count_sec == 9:
    #     count_sec = "09"
    # if count_sec == 8:
    #     count_sec = "08"
    # if count_sec == 7:
    #     count_sec = "07"
    # if count_sec == 6:
    #     count_sec = "06"
    # if count_sec == 5:
    #     count_sec = "05"
    # if count_sec == 4:
    #     count_sec = "04"
    # if count_sec == 3:
    #     count_sec = "03"
    # if count_sec == 2:
    #     count_sec = "02"
    # if count_sec == 1:
    #     count_sec = "01"

    # The same solution as above but shorter:
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(300, count_down, count-1)
    else:
        start_timer()
        global reps
        # global check_label
        if reps % 2 == 0:
            check_label.config(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))
        if reps % 4 == 0:
            check_label.config(text="✔✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))
        if reps % 6 == 0:
            check_label.config(text="✔✔✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))
        if reps % 8 == 0:
            check_label.config(text="✔✔✔✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))
        if reps > 8:
            reps = 0
            check_label.config(text="",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))





#---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



# window.after(1000, )


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# count_down(5)

timer_label = Label(text="Timer", width=11, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
timer_label.grid(column = 1, row = 0)

button_start = Button(text="Start", bg='white', command=start_timer)
button_start.grid(column = 0, row = 2)

# check_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))
check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))
check_label.grid(column = 1, row = 3)

button_reset = Button(text="Reset", bg='white', command=reset_timer)
button_reset.grid(column = 2, row = 2)


window.mainloop()