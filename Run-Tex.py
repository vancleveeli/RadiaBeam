import numpy as np
#import keysight_oscilloscope as ks

from PyTektronixScope import TektronixScope
import tkinter as tk
import matplotlib
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class Oscilliscope():
    def __init__(self, master):
        self.root = master
        #param = self.set_Parameters()
        #temp.destroy()
        super().__init__()
        Channel = 'CH1'
        t0 = 0
        DeltaT = 1e-6
        Param = {Channel, to, DeltaT}
        '''
        self.Channel = Channel
        self.t0 = t0
        self.DeltaT = DeltaT
        '''
        self.root.geometry("800x600")
        self.root.title("Oscilliscope Data")
        #temp.title("Set Parameres")
        t0 = tk.DoubleVar()
        DeltaT = tk.DoubleVar()
        Channel = tk.StringVar()
    
        done = tk.BooleanVar()
        done = False
        self.padding =  {'padx': 15, 'pady': 5}
        # labels
        colbase = 5
        tk.Label(self.root,text = "Channel:").pack()#grid(column = 0 + colbase, row = 0, **self.padding)
        Channel_entry = tk.Entry(self.root, textvariable = Channel)
        Channel_entry.pack()#grid(column = 0 + colbase, row = 1, **self.padding)

        tk.Label(self.root,text = "t0:").pack()#grid(column = 1 + colbase, row = 0, **self.padding)
        t0_entry = tk.Entry(self.root, textvariable = t0)
        t0_entry.pack()#grid(column = 1 + colbase, row = 1, **self.padding)
        
        tk.Label(self.root,text = "Delta t:").pack()#grid(column = 2 + colbase, row = 0, **self.padding)
        DeltaT_entry = tk.Entry(self.root, textvariable = DeltaT)       
        DeltaT_entry.pack()#grid(column = 2 + colbase, row = 1, **self.padding)

        fig = Figure(figsize = (5,5),dpi = 100)
        #dt = preambleBlock['dt']
        #time = dt*np.arange(len(data))
        xdata, ydata = self.read(Channel, t0, DeltaT)
        plot1 = fig.add_subplot(111)
        plot1.plot(xdata, ydata)
        canvas = FigureCanvasTkAgg(fig, master = self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()#grid(column = 2, row = 5, **self.padding)
        
        toolbar = NavigationToolbar2Tk(canvas, self.root)
        toolbar.update()

        done_button = tk.Button(self.root, text = "done", command = self._quit) #self.creat_Widgets())
        done_button.pack(side = 'bottom')#grid(column = 2 + colbase, row = 3, **self.padding)
   
       
    '''
    def startOss(self, resourceName):
        return TektronixScope(resourceName)
    '''
    def read(self, Param): #add OcData when using Oscilliscope
        
        xdata = [i for i in range(101)]
        ydata = [i**2 for i in range(101)]
        
        '''
        scope = TektronixScope(instrument_resource_name)
        xdata,ydata = scope.read_data_one_channel(Param[0], t0 =Param[1], DeltaT = Param[2], x_axis_out=True)
        '''
        return xdata, ydata
    
    
        

    def set_Parameters(self, Param):
        '''
        Channel = ""
        t0 = 0
        DeltaT = 0
        print ("in Parameters")
        padding =  {'padx': 5, 'pady': 5}
        #temp = tk.Tk()
        print ("post temp")
        #temp.title("Set Parameres")
        t0 = tk.DoubleVar()
        DeltaT = tk.DoubleVar()
        Channel = tk.StringVar()
        done = tk.BooleanVar()
        done = False
        print ("post var")
        # labels
        tk.Label(self,text = "Channel:").grid(column = 0, row = 0, **padding)
        tk.Label(temp,text = "t0:").grid(column = 1, row = 0, **padding)
        tk.Label(temp,text = "Delta t:").grid(column = 2, row = 0, **padding)
        print ("post label")
        # Entry
        Channel_entry = tk.Entry(temp, textvariable = Channel)
        t0_entry = tk.Entry(temp, textvariable = t0)
        DeltaT_entry = tk.Entry(temp, textvariable = DeltaT)
        Channel_entry.grid(column = 0, row = 1, **padding)
        t0_entry.grid(column = 1, row = 1, **padding)
        DeltaT_entry.grid(column = 2, row = 1, **padding)
        print ("post Entry")
        done_button = tk.Button(temp, text = "done", command = done == True)
        done_button.grid(column = 2, row = 3, **padding)
        print ("post end")
        while done == False:
            print ()
        '''
        Channel = Param[0]
        t0 = Param[1]
        DeltaT = Param[2]
        return [Channel, t0, DeltaT]

    '''
    def creat_Widgets(self):
        plot_button = tk.Button(master = self.root, command = self.read(self.Channel, self.t0, self.DeltaT), height = 2, width = 10, text = 'Plot')
        #plot_button.pack()
        plot_buttom.pack()#gird(column = 2, row = 4, **self.padding)
        #plot_param = Buttom(master = self.root, command = read(self.Channel, self.t0, self.DeltaT), height = 2, width = 10, text = 'parameters')
        #plot_param.pack()
        
    '''
    '''    
        window = tk.Tk()
        window.geometry("800x600")
        window.title("Oscilliscope Data")
        plot_button = Buttom(master = window, command = read(win, Channel, t0, DeltaT), height = 2, width = 10, text = 'Plot')
        plot_button.pack()
        plot_param = Buttom(master = window, command = read(win, Channel, t0, DeltaT), height = 2, width = 10, text = 'parameters')
        plot_param.pack()
        return window
    '''

    def _quit(self):
        root.quit()     # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    def dest(self):
        root.destroy()

if __name__ == "__main__":
    #dat = startOss()
    root = tk.Tk()
    App = Oscilliscope(root)
    #win = creatWindow(dat)
    
    root.mainloop()