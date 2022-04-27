from tkinter import *
import math

YELLOW = "#f6f3e7"
timer = None
window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW,padx=30, pady=20)
canvas = Canvas(width=500, height=500)
pc_img = PhotoImage(file="pomodoro1.png")
coffee_img = PhotoImage(file="pomodoro2.png")
repeat = 0

def start_timer():
    global repeat
    repeat += 1
    work_sec = 25 * 60
    break_sec = 5 * 60
    break_long_sec = 15 * 60
    if start_btn["state"]:
        start_btn.config(state=DISABLED)
        if repeat % 8 == 0:
            count_down(break_long_sec)
            title.config(text="break...")
            canvas.itemconfig(bg_image, image=coffee_img)
        elif repeat % 2 == 0:
            count_down(break_sec)
            title.config(text="break...")
            canvas.itemconfig(bg_image, image=coffee_img)
        else:
            count_down(work_sec)
            title.config(text="WORK!")
            canvas.itemconfig(bg_image, image=pc_img)


def count_down(count):
    minutes = math.floor(count / 60)
    second = count % 60
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{second}")
    if count > 0:
        global  timer
        timer = window.after(1, count_down, count - 1)
    else:
        start_timer()
        mark =""
        work_sessions = math.floor(repeat/2)
        for _ in range(work_sessions):
            mark +="✔"
        check_mark.config(text=mark)

def stop_timer():
    window.after_cancel(timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(bg_image, image=pc_img)
    check_mark.config(text="")
    start_btn.config(state=NORMAL)
    global repeat
    repeat = 0


bg_image = canvas.create_image(250, 200, image=pc_img)
canvas.config(bg=YELLOW, highlightthickness=0)
timer_text = canvas.create_text(250,360, text="00:00",fill="#333", font=("Futura", 40, "italic"))
canvas.grid(row=1, column=0, rowspan=3, columnspan=3)


title = Label(text="Timer", font=("Futura", 40, "italic"))
title.config(bg=YELLOW)
title.grid(row=0, column=1)

check_mark = Label(text="", font=("Futura", 20, "italic"))
check_mark.config(bg=YELLOW)
check_mark.grid(row=3, column=1)

start_btn = Button(text="start", width=10, highlightbackground=YELLOW, command=start_timer)
start_btn.grid(row=3, column=0,padx=10)

stop_btn = Button(text="stop", width=10, highlightbackground=YELLOW, command=stop_timer)
stop_btn.grid(row=3, column=2)
window.mainloop()