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


def click_mult():
    global operation_sign
    global operation
    global operand_2_value
    operation = '*'
    operand_2_value = '0'
    operation_sign.configure(text=operation)


def click_div():
    global operation_sign
    global operation
    global operand_2_value
    operation = '/'
    operand_2_value = '0'
    operation_sign.configure(text=operation)


def click_eq():
    global operand_1_value
    global operand_2_value

    if operation == '+' and operand_2_value:
        operand_1_value = str(int(operand_1_value) + int(operand_2_value))
    elif operation == '-' and operand_2_value:
        operand_1_value = str(int(operand_1_value) - int(operand_2_value))
    elif operation == '*' and operand_2_value:
        operand_1_value = str(int(operand_1_value) * int(operand_2_value))
    elif operation == '/' and operand_2_value:
        operand_1_value = str(int(operand_1_value) / int(operand_2_value))

    operand_2_value = ''
    operand_1_label.configure(text=operand_1_value)
    operand_2_label.configure(text=operand_2_value)


def click_clear():
    global operand_1_value
    global operand_2_value
    operand_1_value = '0'
    operand_2_value = ''
    operation = ''
    operand_1_label.configure(text=operand_1_value)
    operand_2_label.configure(text=operand_2_value)
    operation_sign.configure(text=operation)


def digit_buttons_gen(n):
    global digit_buttons
    digit_buttons[n] = ttk.Button(window,
                                  text=str(n),
                                  command=lambda: append_digit(n))
    return digit_buttons[n]


digit_buttons = list(range(10))
for i in range(10):
    digit_buttons_gen(i)

digit_buttons[0].grid(column=1, row=2)
digit_buttons[1].grid(column=2, row=2)
digit_buttons[2].grid(column=3, row=2)
digit_buttons[3].grid(column=1, row=3)
digit_buttons[4].grid(column=2, row=3)
digit_buttons[5].grid(column=3, row=3)
digit_buttons[6].grid(column=1, row=4)
digit_buttons[7].grid(column=2, row=4)
digit_buttons[8].grid(column=3, row=4)
digit_buttons[9].grid(column=1, row=5)


button_mult = ttk.Button(window, text='*', command=click_mult)
button_div = ttk.Button(window, text='/', command=click_div)
button_plus = ttk.Button(window, text='+', command=click_plus)
button_minus = ttk.Button(window, text='-', command=click_minus)
button_eq = ttk.Button(window, text='=', command=click_eq)
button_clear = ttk.Button(window, text='Clear', command=click_clear)

button_mult.grid(column=2, row=5)
button_div.grid(column=3, row=5)
button_plus.grid(column=4, row=2)
button_minus.grid(column=4, row=3)
button_eq.grid(column=4, row=4)
button_clear.grid(column=4, row=5)


window.mainloop()
