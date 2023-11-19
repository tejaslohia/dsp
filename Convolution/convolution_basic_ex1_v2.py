import numpy as np
import matplotlib.pyplot as plt

#function for generating Sin Wave
def generateSinWave(amplitude, freq,duration, sampleTime):
    time = np.arange(0, duration, sampleTime)
    sinAmp = amplitude*np.sin(2*np.pi*freq*time)
    return sinAmp, time

def generateRamp(amplitude, duration, sampleTime):
    time = np.arange(0, duration, sampleTime)
    val = amplitude*time/duration;
    return val
    
#Duration and Sample Freq
SAMPLE_FREQ = 1000 #signal2Freq * 20 2000 samples per second
SAMPLE_TIME = 1/SAMPLE_FREQ

#no of samples = SAMPLE_FREQ/SignalFreq
#signal 1 
signal1Freq = 50 
signal1Amp = 1
NO_OF_CYCLE = 3
DURATION = NO_OF_CYCLE/signal1Freq
#generate Two Sinosoidal Signal and Addition of Two Signal
signal1, signal1Time = generateSinWave(signal1Amp, signal1Freq, DURATION, SAMPLE_TIME)

#signal 2
rampPeakValue=8
signal2=generateRamp(rampPeakValue,DURATION,SAMPLE_TIME)

#singal 3
signal3=signal1+signal2

#add 10 element of 0
no_of_zeros=10
a=np.zeros(no_of_zeros)
signal3=np.concatenate((a,signal3))
signal3=np.concatenate((signal3,a))

#low pass filter ()
M=40
n=np.arange(0,M,1)
h=0.54-0.4*np.cos(2*np.pi*n/M)
k=np.sum(h)
h=h/k

#sum=np.sum(h)
conv=np.convolve(signal3,h,mode="full")

xtick_gap=10

def findHlim(datalen,xlim_diff):
    diff_len = xlim_diff - datalen
    count = int(diff_len/2)
    xmin = -1*count
    hmax = xmin + xlim_diff
    return xmin, hmax

# find min and max value for convolution result 
xtick_gap=10
tick_count = int(len(conv)/xtick_gap);
tick_count = tick_count + 1
conv_xmin = 0 
conv_xmax = tick_count * xtick_gap

#fine singal 
signal_xmin, signal_xmax = findHlim(len(signal3),conv_xmax)
h_xmin,h_xmax = findHlim(len(h),conv_xmax)


#ploting waveforms and FFT
fig1=plt.figure("Signal and Convolution")
#plot Singal 1      
plt.subplot(3,1,1)
plt.xlim(signal_xmin,signal_xmax)
plt.xticks(np.arange(signal_xmin,signal_xmax, 10.0))
plt.plot(signal3,'ro')
plt.grid()
plt.title("Sine Wave and Ramp")

#low pass filter
#plot Singal 1      
plt.subplot(3,1,2)
plt.xlim(h_xmin,h_xmax)
plt.xticks(np.arange(h_xmin,h_xmax, 10.0))
plt.plot(h,'ro')
plt.grid()
plt.title("Low Pass Filter")

#result of convolution
plt.subplot(3,1,3)
plt.xlim(conv_xmin,conv_xmax)
plt.xticks(np.arange(conv_xmin,conv_xmax, 10.0))
plt.plot(conv,'ro')
plt.grid()
plt.title("Convolution Result")
plt.show()

#ploting waveforms and FFT
fig2=plt.figure("Signal Generation")
fig1=plt.figure("Signal and Convolution")
#plot Singal 1      
plt.subplot(4,1,1)
plt.plot(signal1,'ro')
plt.grid()
plt.title("Sine Wave Freq 50 Hz")
#plt.show()

#plot Singal 1      
plt.subplot(4,1,2)
plt.plot(signal2,'ro')
plt.grid()
plt.title("Ramp Signal")

#plot Singal 1      
plt.subplot(4,1,3)
plt.plot(signal3,'ro')
plt.grid()
plt.title("Signal")
plt.show()

