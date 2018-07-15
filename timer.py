#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

window = tk.Tk()
window.title("Timer")
window.resizable(False, False)

fixed_font = Font(font='TkFixedFont')

hh = tk.StringVar()
mm = tk.StringVar()
ss = tk.StringVar()

hh.set('00')
mm.set('00')
ss.set('00')


def x_0_plus(obj, limit):
    x_0 = int(obj.get()[0])
    x_0 += 1
    if x_0 > limit:
        x_0 = 0
    obj.set(str(x_0) + obj.get()[1])


def x_0_minus(obj, limit):
    x_0 = int(obj.get()[0])
    x_0 -= 1
    if x_0 < 0:
        x_0 = limit
    obj.set(str(x_0) + obj.get()[1])


def x_1_plus(obj, limit):
    x_1 = int(obj.get()[1])
    x_1 += 1
    if x_1 > limit:
        x_1 = 0
    obj.set(obj.get()[0] + str(x_1))


def x_1_minus(obj, limit):
    x_1 = int(obj.get()[1])
    x_1 -= 1
    if x_1 < 0:
        x_1 = limit
    obj.set(obj.get()[0] + str(x_1))


hh_label = tk.Label(window, text='hh:', font=fixed_font)
hh_label.grid(column=0, row=0, rowspan=2)
mm_label = tk.Label(window, text='mm:', font=fixed_font)
mm_label.grid(column=0, row=2, rowspan=2)
ss_label = tk.Label(window, text='ss:', font=fixed_font)
ss_label.grid(column=0, row=4, rowspan=2)

hh_label_value = tk.Label(window, textvariable=hh, font=fixed_font)
hh_label_value.grid(column=1, row=0, rowspan=2)
mm_label_value = tk.Label(window, textvariable=mm, font=fixed_font)
mm_label_value.grid(column=1, row=2, rowspan=2)
ss_label_value = tk.Label(window, textvariable=ss, font=fixed_font)
ss_label_value.grid(column=1, row=4, rowspan=2)

hh_button_plus_0 = tk.Button(window, text='+',
                             font=fixed_font,
                             command=lambda: x_0_plus(hh, 9))
hh_button_plus_0.grid(column=2, row=0)
hh_button_minus_0 = tk.Button(window, text='-',
                              font=fixed_font,
                              command=lambda: x_0_minus(hh, 9))
hh_button_minus_0.grid(column=2, row=1)

hh_button_plus_1 = tk.Button(window, text='+',
                             font=fixed_font,
                             command=lambda: x_1_plus(hh, 9))
hh_button_plus_1.grid(column=3, row=0)
hh_button_minus_1 = tk.Button(window, text='-',
                              font=fixed_font,
                              command=lambda: x_1_minus(hh, 9))
hh_button_minus_1.grid(column=3, row=1)

mm_button_plus_0 = tk.Button(window, text='+',
                             font=fixed_font,
                             command=lambda: x_0_plus(mm, 5))
mm_button_plus_0.grid(column=2, row=2)
mm_button_minus_0 = tk.Button(window, text='-',
                              font=fixed_font,
                              command=lambda: x_0_minus(mm, 5))
mm_button_minus_0.grid(column=2, row=3)

mm_button_plus_1 = tk.Button(window, text='+',
                             font=fixed_font,
                             command=lambda: x_1_plus(mm, 9))
mm_button_plus_1.grid(column=3, row=2)
mm_button_minus_1 = tk.Button(window, text='-',
                              font=fixed_font,
                              command=lambda: x_1_minus(mm, 9))
mm_button_minus_1.grid(column=3, row=3)

ss_button_plus_0 = tk.Button(window, text='+',
                             font=fixed_font,
                             command=lambda: x_0_plus(ss, 5))
ss_button_plus_0.grid(column=2, row=4)
ss_button_minus_0 = tk.Button(window, text='-',
                              font=fixed_font,
                              command=lambda: x_0_minus(ss, 5))
ss_button_minus_0.grid(column=2, row=5)

ss_button_plus_1 = tk.Button(window, text='+',
                             font=fixed_font,
                             command=lambda: x_1_plus(ss, 9))
ss_button_plus_1.grid(column=3, row=4)
ss_button_minus_1 = tk.Button(window, text='-',
                              font=fixed_font,
                              command=lambda: x_1_minus(ss, 9))
ss_button_minus_1.grid(column=3, row=5)

window.mainloop()
