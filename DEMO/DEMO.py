"""
Demo of a real-time filtering system
The input signal is a ECG recorded 140 seconds
FIR filters are going to eliminate the 50Hz and DC noise
For that purpose the module FIR is employed 
"""

import FIR as fir

"""
Importing the common packages for reading files
and plotting figures
"""

import numpy as np
import matplotlib.pyplot as plt

"""
Gain of the amplifier is 500 (5 from the instrumentation amplifier
and 100 from the non-invertion OP-amp step).

The range of the A/D converter is from -4.096V to 4.096V with 12 bits
"""

ecg=np.loadtxt('ecg.dat')

time=ecg[:,0]

input=ecg[:,1]

input=(input*2-4096)/500

"""
Sampling rate in Hz
"""
Fs=1000.0 
"""
Cut-off frequency of the DC filter in Hz
"""
F0=2.0
"""
First cut-off frequency of the 50Hz filter in Hz
"""  
F1=45.0
"""
Second cut-off frequency of the 50Hz filter in Hz
""" 
F2=55.0   
"""
Normalized equivalent of F0
"""
f0=F0/Fs
"""
Normalized equivalent of F1
"""
f1=F1/Fs
"""
Normalized equivalent of F2
"""
f2=F2/Fs
"""
Number of taps of the DC filter
"""
MDC=100
"""
Number of taps of the 50Hz filter
"""
M50=100

"""
Code to plot the ECG over time:

plt.plot(time,input)
plt.title('ECG recorded in the time domain')
plt.xlabel('time (ms)')
plt.ylabel('amplitude (mV)')

plt.savefig('ecg.pdf')
"""

"""
Code to plot a single beat over time:

input=input[1300:2000]
time=time[1300:2000]

plt.plot(time,input)
plt.title('Heartbeat recorded in the time domain')
plt.xlabel('time (ms)')
plt.ylabel('amplitude (mV)')

plt.savefig('single_heartbeat.pdf')
"""

"""
Instantiating the two filters we are going to use:

    *DC removing filter: filterDC:
        
        -Cut off frequency: f0
        -Number of taps: MDC
        
    *50Hz powerline noise filter: filter50:
            
        -Cut off frequencies: f1 and f2
        -Number of taps: M50
"""
filterDC=fir.FIR()
filter50=fir.FIR()

filterDC.highpass(MDC,f0)
filter50.stopband(M50,f1,f2)

"""
Creating the output vector
"""
output=np.zeros(len(input))

"""
FOR loop which simulates a real time system: every Ts seconds
a new real value input (input[i]) comes to the digital filter
and the system gives a filtered real valued output (output[i])
"""

for i in range(len(input)):
    output[i]=filterDC.filter(input[i])
    output[i]=filter50.filter(output[i])

"""
Saving the output in a data file
"""

np.savetxt('ecg_filtered.dat',output)

"""
Code to plot the ECG filtered over time:

plt.plot(time,output)
plt.title('ECG filtered in the time domain')
plt.xlabel('time (ms)')
plt.ylabel('amplitude (mV)')

plt.savefig('ecg_filtered.pdf')
"""

"""
Code to plot a single beat filtered over time:

output=output[1300+(MDC/2)+(M50/2):2000+(MDC/2)+(M50/2)]#Delay introduced by the filters
time=time[1300+(MDC/2)+(M50/2):2000+(MDC/2)+(M50/2)]

plt.plot(time,output)
plt.title('Heartbeat filtered in the time domain')
plt.xlabel('time (ms)')
plt.ylabel('amplitude (mV)')
plt.savefig('single_heartbeat_filtered.pdf')
"""