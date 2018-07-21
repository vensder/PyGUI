#!/usr/bin/env python3

import tkinter as tk
from tkinter.font import Font
from time import time
from play.sound import bell


window = tk.Tk()
window.title("Timer")
window.resizable(False, False)

fixed_font = Font(font='TkFixedFont')

hh = tk.StringVar()
mm = tk.StringVar()
ss = tk.StringVar()
sss = tk.StringVar()
run_stop_caption = tk.StringVar()

hh.set('00')
mm.set('00')
ss.set('00')
sss.set('000')
run_stop_caption.set('Run')

sss_time_to_stop = 0
display_is_red = False
timer_is_stop = False

def hh_mm_ss_to_sec():
    return int(hh.get()) * 60 * 60 + int(mm.get()) * 60 + int(ss.get())


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


def clear_set():
    global sss_time_to_stop
    global display_is_red
    global timer_is_stop
    hh.set('00')
    mm.set('00')
    ss.set('00')
    sss.set('000')
    run_stop_caption.set('Run')
    sss_time_to_stop = 0
    display_is_red = False


def run_stop():
    global timer_is_stop
    global sss_time_to_stop
    global display_is_red
    global default_color
    if run_stop_caption.get() == 'Run':
        sss.set(str(hh_mm_ss_to_sec()))
        sss_time_now = (int(time()))
        sss_time_to_stop = sss_time_now + hh_mm_ss_to_sec()
        clear_button.config(state='disabled')
        timer_is_stop = False
        sync_sss()
        run_stop_caption.set('Stop')
    elif run_stop_caption.get() == 'Stop':
        timer_is_stop = True
        run_stop_caption.set('Run')
        sss_time_to_stop = 0
        clear_button.config(state='normal')
        display_label.config(bg=default_color)
        display_is_red = False


def sync_sss():
    global timer_is_stop
    if not timer_is_stop:
        global sss_time_to_stop
        global display_is_red
        sss_left = sss_time_to_stop - int(time())
        sss.set(str(sss_left))
        if sss_left <= 0 and not display_is_red:
            display_label.config(bg='red')
            bell()
            display_is_red = True
        window.after(1000, sync_sss)


hh_label = tk.Label(window, text='hh', font=fixed_font)
hh_label.grid(column=0, row=0, columnspan=2)
mm_label = tk.Label(window, text='mm', font=fixed_font)
mm_label.grid(column=2, row=0, columnspan=2)
ss_label = tk.Label(window, text='ss', font=fixed_font)
ss_label.grid(column=4, row=0, columnspan=2)

hh_label_value = tk.Label(window, textvariable=hh, font=fixed_font)
hh_label_value.grid(column=0, row=3, columnspan=2)
mm_label_value = tk.Label(window, textvariable=mm, font=fixed_font)
mm_label_value.grid(column=2, row=3, columnspan=2)
ss_label_value = tk.Label(window, textvariable=ss, font=fixed_font)
ss_label_value.grid(column=4, row=3, columnspan=2)

hh_button_plus_0 = tk.Button(window, text='+', font=fixed_font,
                             command=lambda: x_0_plus(hh, 9))
hh_button_minus_0 = tk.Button(window, text='-', font=fixed_font,
                              command=lambda: x_0_minus(hh, 9))
hh_button_plus_0.grid(column=0, row=1)
hh_button_minus_0.grid(column=0, row=4)

hh_button_plus_1 = tk.Button(window, text='+', font=fixed_font,
                             command=lambda: x_1_plus(hh, 9))
hh_button_minus_1 = tk.Button(window, text='-', font=fixed_font,
                              command=lambda: x_1_minus(hh, 9))
hh_button_plus_1.grid(column=1, row=1)
hh_button_minus_1.grid(column=1, row=4)

mm_button_plus_0 = tk.Button(window, text='+', font=fixed_font,
                             command=lambda: x_0_plus(mm, 5))
mm_button_minus_0 = tk.Button(window, text='-', font=fixed_font,
                              command=lambda: x_0_minus(mm, 5))
mm_button_plus_0.grid(column=2, row=1)
mm_button_minus_0.grid(column=2, row=4)

mm_button_plus_1 = tk.Button(window, text='+', font=fixed_font,
                             command=lambda: x_1_plus(mm, 9))
mm_button_minus_1 = tk.Button(window, text='-', font=fixed_font,
                              command=lambda: x_1_minus(mm, 9))
mm_button_plus_1.grid(column=3, row=1)
mm_button_minus_1.grid(column=3, row=4)

ss_button_plus_0 = tk.Button(window, text='+', font=fixed_font,
                             command=lambda: x_0_plus(ss, 5))
ss_button_minus_0 = tk.Button(window, text='-', font=fixed_font,
                              command=lambda: x_0_minus(ss, 5))
ss_button_plus_0.grid(column=4, row=1)
ss_button_minus_0.grid(column=4, row=4)

ss_button_plus_1 = tk.Button(window, text='+', font=fixed_font,
                             command=lambda: x_1_plus(ss, 9))
ss_button_minus_1 = tk.Button(window, text='-', font=fixed_font,
                              command=lambda: x_1_minus(ss, 9))
ss_button_plus_1.grid(column=5, row=1)
ss_button_minus_1.grid(column=5, row=4)

clear_button = tk.Button(window, text='Clr', font=fixed_font,
                         command=lambda: clear_set())
clear_button.grid(column=0,row=5, columnspan=2)

start_button = tk.Button(window, textvariable=run_stop_caption, font=fixed_font,
                         command=lambda: run_stop())
start_button.grid(column=2,row=5, columnspan=2)

display_label = tk.Label(window, textvariable=sss, font=fixed_font)
display_label.grid(column=4, row=5, columnspan=2)
default_color = display_label.cget('bg')

window.mainloop()
