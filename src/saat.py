from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("My Digital Time")
app_window.geometry("650x450")
app_window.resizable(30,30)

text_font= ("Boulder", 48, 'bold')
background = "Black"
foreground = "White"
border_width = 200

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=0)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(100, digital_clock)

digital_clock()
