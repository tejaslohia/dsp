#import library
import numpy as np
import matplotlib.pyplot as plt


def signaltonoise(Arr, axis=0, ddof=0):
    Arr = np.asanyarray(Arr)
    me = Arr.mean(axis)
    sd = Arr.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, me/sd)
#Arr=[[20, 4, 7, 1, 34], [50, 12, 15, 34, 5]]
#print(signaltonoise(Arr,axis=0,ddof=0))

#Duration and Sample Freq
#DURATION = 1.024 # 5 peak for 50 and 10 peak for 100
DURATION = 0.512 # 5 peak for 50 and 10 peak for 100
SAMPLE_FREQ = 100*20 #signal2Freq * 20 2000 samples per second
SAMPLE_TIME = 1/SAMPLE_FREQ

#function for generating Sin Wave
def generateSinWave(amplitude,freq,duration,sampleTime):
    time=np.arange(0,duration,sampleTime)
    sinAmp=amplitude*np.sin(2*np.pi*freq*time)
    return sinAmp,time

#signal 1 and 2 :  Amp and Freq
signal1Freq = 10
signal1Amp = 10
signal2Freq = 800
signal2Amp = 2

#generate Two Sinosoidal Signal and Addition of Two Signal
signal1,signal1Time=generateSinWave(signal1Amp,signal1Freq,DURATION,SAMPLE_TIME) #5 samples for 50

'''
#ploting waveforms and FFT
fig1=plt.figure("Signal and FFT")
#plot Singal 1      
plt.plot(signal1Time,signal1,color='green')
plt.grid()
plt.title("Sine Wave Freq 50 Hz")
print(len(signal1))
plt.show()
'''
x_volts=signal1
t=signal1Time

x_watts = x_volts ** 2
x_db = 10 * np.log10(x_watts)

# Adding noise using target SNR

# Set a target SNR
target_snr_db = 20
# Calculate signal power and convert to dB 
sig_avg_watts = np.mean(x_watts)
sig_avg_db = 10 * np.log10(sig_avg_watts)
# Calculate noise according to [2] then convert to watts
noise_avg_db = sig_avg_db - target_snr_db
noise_avg_watts = 10 ** (noise_avg_db / 10)
# Generate an sample of white noise
mean_noise = 0
noise_volts = np.random.normal(mean_noise, np.sqrt(noise_avg_watts), len(x_watts))
# Noise up the original signal
y_volts = x_volts + noise_volts

y_watts = y_volts ** 2
y_db = 10 * np.log10(y_watts)

'''
plt.subplot(2,1,2)
plt.plot(t, 10* np.log10(y_volts**2))
plt.title('Signal with noise (dB)')
plt.ylabel('Power (dB)')
plt.xlabel('Time (s)')
plt.show()
'''
## added by tejas lohia for fft
#calculate FFT using np library
sigfft=np.fft.fft(y_volts)
#normalize to show amplitude on fft plot
sigfft=sigfft*2/(len(y_volts))

#calculate half length for ploting
fftLen=len(y_volts)
halfFFTLen=int(fftLen/2)
count=np.arange(halfFFTLen)
#generate freq and half fft for plot  
freq = count * SAMPLE_FREQ/fftLen;
sigFFTHalf=sigfft[range(halfFFTLen)]

absfft=abs(sigFFTHalf)
max=np.argmax(absfft)
maxv=absfft[max]

Pn=0
for i in range(halfFFTLen):
#    if i != max:
    v=absfft[i]
    Pn=Pn+(v*v)/2

Pn=Pn/fftLen

Ps=absfft[max]*absfft[max]/2
ratio=Ps/Pn
snr=10*np.log10(ratio)

Ps_db = 10 * np.log10(Ps)
Pn_db = 10 * np.log10(Pn)
snr1=Ps_db-Pn_db

snr2=signaltonoise(y_volts)

#The sampling time is the time interval between successive samples, also called the sampling interval or the sampling period, and denoted T
#The sampling rate is the number of samples per second. It is the reciprocal of the sampling time, i.e. 1/T also called the sampling frequency, and denoted Fs
#The frequency axis for the FFT is linked to the number N
#of points in the DFT and the sampling rate Fs. It is defined as f=k⋅FsN. With k going up to N

#ploting waveforms and FFT
fig2=plt.figure("Signal and FFT")

#plot Singal 1      
plt.subplot(4,1,1)
plt.plot(signal1Time,signal1,color='green')
plt.grid()
plt.title("Sine Wave Freq 50 Hz")

plt.subplot(4,1,2)
plt.plot(t, y_volts)
plt.title('Signal with noise')
plt.ylabel('Voltage (V)')
plt.xlabel('Time (s)')
plt.grid()

plt.subplot(4,1,3)
plt.plot(t, 10* np.log10(y_volts**2))
plt.title('Signal with noise (dB)')
plt.ylabel('Power (dB)')
plt.xlabel('Time (s)')
plt.grid()

#plot FFT
plt.subplot(4,1,4)
plt.plot(freq,abs(sigFFTHalf),'ro')
plt.grid()
plt.title("FFT")

plt.show()