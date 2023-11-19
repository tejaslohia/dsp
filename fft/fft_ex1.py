#import library
import numpy as np
import matplotlib.pyplot as plt

#Duration and Sample Freq
DURATION = 0.1 # 5 peak for 50 and 10 peak for 100
SAMPLE_FREQ = 100*20 #signal2Freq * 20 2000 samples per second
SAMPLE_TIME = 1/SAMPLE_FREQ

#function for generating Sin Wave
def generateSinWave(amplitude,freq,duration,sampleTime):
    time=np.arange(0,duration,sampleTime)
    sinAmp=amplitude*np.sin(2*np.pi*freq*time)
    return sinAmp,time

#signal 1 and 2 :  Amp and Freq
signal1Freq = 50
signal1Amp = 10
signal2Freq = 800
signal2Amp = 2

#generate Two Sinosoidal Signal and Addition of Two Signal
signal1,signal1Time=generateSinWave(signal1Amp,signal1Freq,DURATION,SAMPLE_TIME) #5 samples for 50
signal2,signal2Time=generateSinWave(signal2Amp,signal2Freq,DURATION,SAMPLE_TIME) 
#adding both singals
signal_add = signal1 + signal2

#make first sample ampplitude of signle 2 to plot with same height on plot
signal2[0]=signal1Amp #just for plot

#calculate FFT using np library
sigfft=np.fft.fft(signal_add)
#normalize to show amplitude on fft plot
sigfft=sigfft*2/(len(signal_add))

#calculate half length for ploting
fftLen=len(sigfft)
halfFFTLen=int(fftLen/2)
count=np.arange(halfFFTLen)
#generate freq and half fft for plot  
freq = count * SAMPLE_FREQ/fftLen;
sigFFTHalf=sigfft[range(halfFFTLen)]

#The sampling time is the time interval between successive samples, also called the sampling interval or the sampling period, and denoted T
#The sampling rate is the number of samples per second. It is the reciprocal of the sampling time, i.e. 1/T also called the sampling frequency, and denoted Fs
#The frequency axis for the FFT is linked to the number N
#of points in the DFT and the sampling rate Fs. It is defined as f=k⋅FsN. With k going up to N

#ploting waveforms and FFT
fig1=plt.figure("Signal and FFT")

#plot Singal 1      
plt.subplot(4,1,1)
plt.plot(signal1Time,signal1,color='green')
plt.grid()
plt.title("Sine Wave Freq 50 Hz")

#plot Singal 2
plt.subplot(4,1,2)
plt.plot(signal2Time,signal2,color='green')
plt.grid()
plt.title("Sine Wave Freq 100 Hz")

#plot Singal Addition
plt.subplot(4,1,3)
plt.plot(signal2Time,signal_add,color='green')
plt.grid()
plt.title("Sine Wave Freq 50 & 100 Hz")

#plot FFT
plt.subplot(4,1,4)
plt.plot(freq,abs(sigFFTHalf),'ro')
plt.grid()
plt.title("FFT")

plt.show()

#def signaltonoise(a, axis=0, ddof=0):
#    a = np.asanyarray(a)
#    m = a.mean(axis)
#    sd = a.std(axis=axis, ddof=ddof)
#    return np.where(sd == 0, 0, m/sd)
#snr=signaltonoise(signal_add)
#print(snr)