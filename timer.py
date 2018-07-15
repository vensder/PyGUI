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


def h_0_plus():
    h_0 = int(hh.get()[0])
    h_0 += 1
    if h_0 > 9:
        h_0 = 0
    hh.set(str(h_0) + hh.get()[1])


def h_1_plus():
    h_1 = int(hh.get()[1])
    h_1 += 1
    if h_1 > 9:
        h_1 = 0
    hh.set(hh.get()[0] + str(h_1))


def h_0_minus():
    h_0 = int(hh.get()[0])
    h_0 -= 1
    if h_0 < 0:
        h_0 = 9
    hh.set(str(h_0) + hh.get()[1])


def h_1_minus():
    h_1 = int(hh.get()[1])
    h_1 -= 1
    if h_1 < 0:
        h_1 = 9
    hh.set(hh.get()[0] + str(h_1))


def m_0_plus():
    m_0 = int(mm.get()[0])
    m_0 += 1
    if m_0 > 5:
        m_0 = 0
    mm.set(str(m_0) + mm.get()[1])


def m_1_plus():
    m_1 = int(mm.get()[1])
    m_1 += 1
    if m_1 > 9:
        m_1 = 0
    mm.set(mm.get()[0] + str(m_1))


def m_0_minus():
    m_0 = int(mm.get()[0])
    m_0 -= 1
    if m_0 < 0:
        m_0 = 5
    mm.set(str(m_0) + mm.get()[1])


def m_1_minus():
    m_1 = int(mm.get()[1])
    m_1 -= 1
    if m_1 < 0:
        m_1 = 9
    mm.set(mm.get()[0] + str(m_1))


def s_0_plus():
    s_0 = int(ss.get()[0])
    s_0 += 1
    if s_0 > 5:
        s_0 = 0
    ss.set(str(s_0) + ss.get()[1])


def s_1_plus():
    s_1 = int(ss.get()[1])
    s_1 += 1
    if s_1 > 9:
        s_1 = 0
    ss.set(ss.get()[0] + str(s_1))


def s_0_minus():
    s_0 = int(ss.get()[0])
    s_0 -= 1
    if s_0 < 0:
        s_0 = 5
    ss.set(str(s_0) + ss.get()[1])


def s_1_minus():
    s_1 = int(ss.get()[1])
    s_1 -= 1
    if s_1 < 0:
        s_1 = 9
    ss.set(ss.get()[0] + str(s_1))


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

hh_button_plus_0 = tk.Button(window, text='+', font=fixed_font, command=h_0_plus)
hh_button_plus_0.grid(column=2, row=0)
hh_button_minus_0 = tk.Button(window, text='-', font=fixed_font, command=h_0_minus)
hh_button_minus_0.grid(column=2, row=1)

hh_button_plus_1 = tk.Button(window, text='+', font=fixed_font, command=h_1_plus)
hh_button_plus_1.grid(column=3, row=0)
hh_button_minus_1 = tk.Button(window, text='-', font=fixed_font, command=h_1_minus)
hh_button_minus_1.grid(column=3, row=1)

mm_button_plus_0 = tk.Button(window, text='+', font=fixed_font, command=m_0_plus)
mm_button_plus_0.grid(column=2, row=2)
mm_button_minus_0 = tk.Button(window, text='-', font=fixed_font, command=m_0_minus)
mm_button_minus_0.grid(column=2, row=3)

mm_button_plus_1 = tk.Button(window, text='+', font=fixed_font, command=m_1_plus)
mm_button_plus_1.grid(column=3, row=2)
mm_button_minus_1 = tk.Button(window, text='-', font=fixed_font, command=m_1_minus)
mm_button_minus_1.grid(column=3, row=3)

ss_button_plus_0 = tk.Button(window, text='+', font=fixed_font, command=s_0_plus)
ss_button_plus_0.grid(column=2, row=4)
ss_button_minus_0 = tk.Button(window, text='-', font=fixed_font, command=s_0_minus)
ss_button_minus_0.grid(column=2, row=5)

ss_button_plus_1 = tk.Button(window, text='+', font=fixed_font, command=s_1_plus)
ss_button_plus_1.grid(column=3, row=4)
ss_button_minus_1 = tk.Button(window, text='-', font=fixed_font, command=s_1_minus)
ss_button_minus_1.grid(column=3, row=5)

window.mainloop()
