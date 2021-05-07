import numpy as np
import keysight_oscilloscope as ks
import tkinter as tk
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import matplotlib.pyplot as plt


def startOss():
    return ks.Oscilloscope()

def read(OcData):
    data, preambleBlock = OcData.get_timetrace()
    fig = Figure(figsize = (5,5),dpi = 100)
    dt = preambleBlock['dt']
    time = dt*np.arange(len(data))
    plot1 = fig.add_subplot(111)
    plot1.plot(time, data)

    canvas = FigureCanvasTkAgg(fig, master = window)
    canvus.draw()

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    
    canvus.get_tk_widget().pack()

def param(OC,parameters):
    OC.update(parametrs)
#    return OC

def creatWindow(win):
    window = tk.Tk()
    window.geometry("800x600")
    window.title("Oscilliscope Data")
    plot_button = Buttom(master = window, command = read(win), height = 2, width = 10, text = 'Plot')
    plot_button.pack()
    plot_param = Buttom(master = window, command = read(win), height = 2, width = 10, text = 'parameters')
    plot_param.pack()
    return window


dat = startOss()

win = creatWindow(dat)

win.mainloop()