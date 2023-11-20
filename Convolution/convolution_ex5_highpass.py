import numpy as np
import matplotlib.pyplot as plt

#function for generating Sin Wave
def generateSinWave(amplitude,freq,duration,sampleTime):
    time=np.arange(0,duration,sampleTime)
    sinAmp=amplitude*np.sin(2*np.pi*freq*time)
    return sinAmp,time

def generateRamp(amplitude,duration,sampleTime):
    time=np.arange(0,duration,sampleTime)
    val=amplitude*time/duration;
    return(val)
    
#Duration and Sample Freq
SAMPLE_FREQ = 1000 #signal2Freq * 20 2000 samples per second
SAMPLE_TIME = 1/SAMPLE_FREQ

#no of samples = SAMPLE_FREQ/SignalFreq
#signal 1 
signal1Freq = 50 
signal1Amp = 1
NO_OF_CYCLE=3
DURATION = NO_OF_CYCLE/signal1Freq
#generate Two Sinosoidal Signal and Addition of Two Signal
signal1,signal1Time=generateSinWave(signal1Amp,signal1Freq,DURATION,SAMPLE_TIME)

#signal 2
rampPeakValue=8
signal2=generateRamp(rampPeakValue,DURATION,SAMPLE_TIME)

#singal 3
signal3=signal1+signal2

no_of_zeros=0
#add 10 element of 0
'''
no_of_zeros=10
a=np.zeros(no_of_zeros)
signal3=np.concatenate((a,signal3))
signal3=np.concatenate((signal3,a))
'''

#High pass filter ()
M=20
n=np.ones(M)
n=n*-0.05
index=int(M/2)
n[index]=0
sum=np.sum(n)
n[index]=sum*-1;
h=n

#sum=np.sum(h)
conv=np.convolve(signal3,h,mode="same")

#finding x limit for M display 
count=int((len(signal3)-M)/2)
conv_xlim_min=-1*count-no_of_zeros;
conv_xlim_max=len(signal2)+count+no_of_zeros;

#ploting waveforms and FFT
fig1=plt.figure("Signal and Convolution")
#plot Singal 1      
plt.subplot(3,1,1)
plt.plot(signal3,'ro')
plt.grid()
plt.title("Sine Wave and Ramp")

#low pass filter
#plot Singal 1      
plt.subplot(3,1,2)
plt.xlim(conv_xlim_min,conv_xlim_max)
plt.plot(h,'ro')
plt.grid()
plt.title("Low Pass Filter")

plt.subplot(3,1,3)
plt.plot(conv,'ro')
plt.grid()
plt.title("Convolution Result")
plt.show()


'''
#ploting waveforms and FFT
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
'''
