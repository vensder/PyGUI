#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)
operand_1_value = '0'
operand_2_value = ''
operation = ''

operand_1_label = ttk.Label(window, text='0')
operand_1_label.grid(column=1, row=0, columnspan=3, sticky='e')

operand_2_label = ttk.Label(window, text='')
operand_2_label.grid(column=1, row=1, columnspan=3, sticky='e')

operation_sign = ttk.Label(window, text=operation)
operation_sign.grid(column=4, row=0, rowspan=2)


def append_digit(digit):
    global operand_1_value
    global operand_2_value

    if operand_2_value:
        operand_2_value += str(digit)
        operand_2_value = str(int(operand_2_value))
        operand_2_label.configure(text=operand_2_value)
    else:
        operand_1_value += str(digit)
        operand_1_value = str(int(operand_1_value))
        operand_1_label.configure(text=operand_1_value)


def click_plus():
    global operation_sign
    global operation
    global operand_2_value
    operation = '+'
    operand_2_value = '0'
    operation_sign.configure(text=operation)


def click_minus():
    global operation_sign
    global operation
    global operand_2_value
    operation = '-'
    operand_2_value = '0'
    operation_sign.configure(text=operation)


def click_eq():
    global operand_1_value
    global operand_2_value
    if operation == '+' and operand_2_value:
        operand_1_value = str(int(operand_1_value) + int(operand_2_value))
    elif operation == '-' and operand_2_value:
        operand_1_value = str(int(operand_1_value) - int(operand_2_value))

    operand_2_value = ''
    operand_1_label.configure(text=operand_1_value)
    operand_2_label.configure(text=operand_2_value)


def click_0():
    append_digit(0)


def click_1():
    append_digit(1)


def click_2():
    append_digit(2)


def click_3():
    append_digit(3)


def click_4():
    append_digit(4)


def click_5():
    append_digit(5)


button_0 = ttk.Button(window, text="0", command=click_0)
button_1 = ttk.Button(window, text="1", command=click_1)
button_2 = ttk.Button(window, text="2", command=click_2)
button_3 = ttk.Button(window, text="3", command=click_3)
button_4 = ttk.Button(window, text="4", command=click_4)
button_5 = ttk.Button(window, text="5", command=click_5)

button_plus = ttk.Button(window, text='+', command=click_plus)
button_minus = ttk.Button(window, text='-', command=click_minus)
button_eq = ttk.Button(window, text='=', command=click_eq)

button_0.grid(column=1, row=2)
button_1.grid(column=2, row=2)
button_2.grid(column=3, row=2)
button_3.grid(column=1, row=3)
button_4.grid(column=2, row=3)
button_5.grid(column=3, row=3)
button_plus.grid(column=4, row=2)
button_minus.grid(column=4, row=3)
button_eq.grid(column=4, row=4)


window.mainloop()
