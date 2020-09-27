#!/usr/bin/env python3


# (0°C × 9/5) + 32 = 32°F
# [°C] = ([°F] − 32) × ​5⁄9
# [°F] = [°C] × ​9⁄5 + 32

from tkinter import *


def fahr(x):
    return round(float(x) * (9.0 / 5) + 32.0, 1)


def set_label_text(f):
    label.config(text=str(fahr(f)) + "°F")


root = Tk()
var = DoubleVar()
label = Label(root, text=str(fahr(0)))

scale = Scale(root, from_=200, to=-100, resolution=0.1, length=300)
scale.pack(anchor=CENTER)
scale.config(command=set_label_text, label="°C")


label.pack()

root.mainloop()
