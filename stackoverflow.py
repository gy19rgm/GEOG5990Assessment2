# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:03:39 2020

Author: R Martin, The University of Leeds, 201369797

"""
# Embed a pyplot in a tkinter window and update it - stackoverflow
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import matplotlib.pyplot as mpl
import numpy as np

root = tkinter.Tk()
root.wm_title("White Star Line icebergs")

fig = mpl.figure(1)
t = np.arange(0.0,3.0,0.01)
s = np.sin(np.pi*t)
mpl.plot(t,s)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def close():
    root.destroy()

button = tkinter.Button(master=root, text="Exit", command=close)
button.pack(side=tkinter.BOTTOM)

menubar = tkinter.Menu(root)
root.config(menu=menubar)
model_menu = tkinter.Menu(menubar)
menubar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Close model", command=close)

tkinter.mainloop()













# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:05:08 2020

@author: Perfe
"""
'''
# placing pot in tkinter main window in python - stackoverflow
__author__ = 'Dania'
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

class mclass:
    def __init__(self,  window):
        self.window = window
        self.box = Entry(window)
        self.button = Button (window, text="check", command=self.plot)
        self.box.pack ()
        self.button.pack()

    def plot (self):
        x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
        p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
            19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])

        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.scatter(v,x,color='red')
        a.plot(p, range(2 +max(x)),color='blue')
        a.invert_yaxis()

        a.set_title ("Estimation Grid", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

window= Tk()
start= mclass (window)
window.mainloop()
'''
'''
import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
# Implement the default Matplotlib key bindings.
#from matplotlib.backend_bases import key_press_handler
#from matplotlib.figure import Figure
import matplotlib.pyplot as mpl

import numpy as np

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

#fig = Figure(figsize=(5, 4), dpi=100)
#t = np.arange(0, 3, .01)
#fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

#t = np.arange(0.0, 2.0, 0.01)
#s = 1 + np.sin(2 * np.pi * t)
#fig, ax = mpl.subplots()
#ax.plot(t, s)
#ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#       title='About as simple as it gets, folks')
#ax.grid()

fig = mpl.figure(1)
t = np.arange(0.0,3.0,0.01)
s = np.sin(np.pi*t)
mpl.plot(t,s)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def close():
    root.destroy()

button = tkinter.Button(master=root, text="Quit", command=close)
button.pack(side=tkinter.BOTTOM)

menubar = tkinter.Menu(root)
root.config(menu=menubar)
model_menu = tkinter.Menu(menubar)
menubar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Close model", command=close)

tkinter.mainloop()
'''


