#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
win.resizable(False, False)

label_text = "A"
a_label = ttk.Label(win, text="   A   L A B E L   ")
a_label.grid(column=0, row=0)


def click_me():
    global label_text
    label_text += "A"
    action.configure(text="I hav been clicked!")
    a_label.configure(foreground='red')
    a_label.configure(text=label_text)


action = ttk.Button(win, text="Click me!", command=click_me)
action.grid(column=1, row=0)

win.mainloop()
