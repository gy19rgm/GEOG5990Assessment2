# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:03:39 2020

Author: R Martin, The University of Leeds, 201369797

"""

# import libraries
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.colors
import matplotlib.pyplot as mpl
import tkinter
from matplotlib.figure import Figure

fig = matplotlib.pyplot.figure(figsize=(5, 5))
#ax = fig.add_axes([0, 0, 1, 1])





def run():

    animation = matplotlib.animation.FuncAnimation(fig, repeat=False)
    canvas.draw()

def close():

    root.destroy()

# Set up GUI
root = tkinter.Tk()
root.wm_title("White Star Line Iceberg Findings")
canvas = tkinter.Canvas(root, width = 500, height = 500)
canvas.pack()

menubar = tkinter.Menu(root)
root.config(menu=menubar)
model_menu = tkinter.Menu(menubar)
menubar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run, state="normal")
model_menu.add_command(label="Close model", command=close)

tkinter.mainloop()