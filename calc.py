#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)
value_1 = '0'
value_2 = ''
operation = ''

operand_1 = ttk.Label(window, text='0')
operand_1.grid(column=1, row=0, columnspan=3, sticky='e')

operand_2 = ttk.Label(window, text='')
operand_2.grid(column=1, row=1, columnspan=3, sticky='e')

operation_sign = ttk.Label(window, text=operation)
operation_sign.grid(column=4, row=0, rowspan=2)


def append_num(num):
    global value_1
    global value_2

    if value_2:
        value_2 += str(num)
        value_2 = str(int(value_2))
        operand_2.configure(text=value_2)
    else:
        value_1 += str(num)
        value_1 = str(int(value_1))
        operand_1.configure(text=value_1)


def click_plus():
    global operation_sign
    global operation
    global value_2
    operation = '+'
    value_2 = '0'
    operation_sign.configure(text=operation)


def click_eq():
    global value_1
    global value_2
    if operation == '+' and value_2:
        value_1 = str(int(value_1) + int(value_2))
        value_2 = ''

    operand_1.configure(text=value_1)
    operand_2.configure(text=value_2)


def click_0():
    append_num(0)


def click_1():
    append_num(1)


def click_2():
    append_num(2)


def click_3():
    append_num(3)


def click_4():
    append_num(4)


def click_5():
    append_num(5)


button_0 = ttk.Button(window, text="0", command=click_0)
button_1 = ttk.Button(window, text="1", command=click_1)
button_2 = ttk.Button(window, text="2", command=click_2)
button_3 = ttk.Button(window, text="3", command=click_3)
button_4 = ttk.Button(window, text="4", command=click_4)
button_5 = ttk.Button(window, text="5", command=click_5)
button_plus = ttk.Button(window, text='+', command=click_plus)
button_eq = ttk.Button(window, text='=', command=click_eq)

button_0.grid(column=1, row=2)
button_1.grid(column=2, row=2)
button_2.grid(column=3, row=2)
button_3.grid(column=1, row=3)
button_4.grid(column=2, row=3)
button_5.grid(column=3, row=3)
button_plus.grid(column=4, row=2)
button_eq.grid(column=4, row=3)


window.mainloop()
