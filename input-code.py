import visa
import numpy as np
from struct import unpack
import pylab

# Establish Connection
rm = visa.ResourceManager('@py') # Calling PyVisaPy library
#scope = rm.open_resource('USB0::0x0699::0x0409::C010730::INSTR') # Connecting via USB
scope = rm.open_resource('TCPIP::192.16.13.181::INSTR') # Connecting via LAN 
 
# Setting source as Channel 1
scope.write('DATA:SOU CH1') 
scope.write('DATA:WIDTH 1') 
scope.write('DATA:ENC RPB')

# Getting axis info
ymult = float(scope.query('WFMPRE:YMULT?')) # y-axis least count
yzero = float(scope.query('WFMPRE:YZERO?')) # y-axis zero error
yoff = float(scope.query('WFMPRE:YOFF?')) # y-axis offset
xincr = float(scope.query('WFMPRE:XINCR?')) # x-axis least count

# Reading Binary Data from instrument
scope.write('CURVE?')
data = scope.read_raw() # Reading binary data
headerlen = 2 + int(data[1]) # Finding header length
header = data[:headerlen] # Separating header 
ADC_wave = data[headerlen:-1] # Separating data

# Converting to Binary to ASCII
ADC_wave = np.array(unpack('%sB' % len(ADC_wave),ADC_wave))

Volts = (ADC_wave - yoff) * ymult + yzero
Time = np.arange(0, xincr * len(Volts), xincr)

# Plotting Volt Vs. Time
pylab.plot(Time, Volts) 
pylab.show()