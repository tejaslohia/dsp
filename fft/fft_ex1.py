import numpy as np
import matplotlib.pyplot as plt

#def signaltonoise(a, axis=0, ddof=0):
#    a = np.asanyarray(a)
#    m = a.mean(axis)
#    sd = a.std(axis=axis, ddof=ddof)
#    return np.where(sd == 0, 0, m/sd)


def generateSinWave(amplitude,freq,duration,sampleTime):
    time=np.arange(0,duration,sampleTime)
    sinAmp=amplitude*np.sin(2*np.pi*freq*time)
    return sinAmp,time

signal1Freq = 50
signal1Amp = 10

signal2Freq = 800
signal2Amp = 2

DURATION = 0.1 # 5 peak for 50 and 10 peak for 100
SAMPLE_FREQ = 100*20 #signal2Freq * 20 2000 samples per second
SAMPLE_TIME = 1/SAMPLE_FREQ

signal1,signal1Time=generateSinWave(signal1Amp,signal1Freq,DURATION,SAMPLE_TIME) #5 samples for 50
signal2,signal2Time=generateSinWave(signal2Amp,signal2Freq,DURATION,SAMPLE_TIME) 

signal2[0]=signal1Amp

signal_add = signal1 + signal2

#print(signal1)
#print(signal1Time)
fig1=plt.figure("figure 1")
plt.subplot(4,1,1)
plt.plot(signal1Time,signal1,color='green')
plt.grid()
plt.title("Sine Wave Freq 50 Hz")

plt.subplot(4,1,2)
plt.plot(signal2Time,signal2,color='green')
plt.grid()
plt.title("Sine Wave Freq 100 Hz")

plt.subplot(4,1,3)
plt.plot(signal2Time,signal_add,color='green')
plt.grid()
plt.title("Sine Wave Freq 50 & 100 Hz")

plt.subplot(4,1,4)
#fig1=plt.figure("figure 2")
sigfft=np.fft.fft(signal_add)*2/(len(signal_add))

fftLen=len(sigfft)

halfFFTLen=int(fftLen/2)
count=np.arange(halfFFTLen)

freq = count * SAMPLE_FREQ/fftLen;
sigFFTHalf=sigfft[range(halfFFTLen)]

plt.plot(freq,abs(sigFFTHalf),'ro')
plt.grid()
plt.title("FFT")

plt.show()
#print(freq)

#The sampling time is the time interval between successive samples, also called the sampling interval or the sampling period, and denoted T
#The sampling rate is the number of samples per second. It is the reciprocal of the sampling time, i.e. 1/T also called the sampling frequency, and denoted Fs
#The frequency axis for the FFT is linked to the number N
#of points in the DFT and the sampling rate Fs. It is defined as f=k⋅FsN. With k going up to N
plt.show()

#snr=signaltonoise(signal_add)
#print(snr)



