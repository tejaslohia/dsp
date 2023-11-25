
import numpy as np
import matplotlib.pyplot as plt

def generate_sinusoidal_signal(frequency, amplitude, duration, sampling_rate):
    t = np.arange(0, duration, 1/sampling_rate)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, signal

def calculate_power(signal):
    magnitude_squared = np.abs(signal)**2
    average_power = np.mean(magnitude_squared)
    return average_power

# Parameters for the first sinusoidal signal
frequency_1 = 5.0
amplitude_1 = 10.0

# Parameters for the second sinusoidal signal
frequency_2 = 100.0
amplitude_2 = 1.0

# Common parameters for both signals
duration = 1.0
sampling_rate = 1024

# Generate two sinusoidal signals
t1, signal1 = generate_sinusoidal_signal(frequency_1, amplitude_1, duration, sampling_rate)
t2, signal2 = generate_sinusoidal_signal(frequency_2, amplitude_2, duration, sampling_rate)

# Combine the two signals
combined_signal = signal1 + signal2

# Plot the signals
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t1, signal1, label='Signal 1')
plt.legend()
plt.subplot(3, 1, 2)
plt.plot(t2, signal2, label='Signal 2')
plt.legend()
plt.subplot(3, 1, 3)
plt.plot(t1, combined_signal, label='Combined Signal')
plt.legend()
#plt.show()

# Calculate power of the combined signal
power1=calculate_power(signal1)
power2=calculate_power(signal2)
power_combined = calculate_power(combined_signal)
print(f"Signal 1 Power : {power1}")
print(f"Signal 2 Power : {power2}")
print(f"Combined Signal Power : {power_combined}")
#other way of calculating power of two signal
print(f"Signal 1 Power : {amplitude_1**2/2}")
print(f"Signal 2 Power : {amplitude_2**2/2}")
snr_sin=10*np.log10(power1/power2)
print("SNR : ",snr_sin)

# FFT of combined signal
sigFFT=np.fft.fft(combined_signal)
fftLen=len(sigFFT)
#normalizing sigFFT
sigFFT=np.abs(sigFFT*2/fftLen)

#normalized half sinnal
sigFFTHalf=sigFFT[range((int)(fftLen/2))]

#plot singal
plt.figure(figsize=(10, 6))
plt.plot(sigFFTHalf)
plt.show()
#calculate power of total signal
power=np.sum(sigFFTHalf**2/2)
print("FFT : Total Power : ",power)

#calculate power of orig signal
frequency_index = np.argmax(sigFFTHalf)
signalAmp = sigFFTHalf[frequency_index]
signal_power=signalAmp**2/2
noise_power=power-signal_power
snr_fft=10*np.log10(signal_power/noise_power)
print(f"FFT : Singal Power : {signal_power}")
print(f"FFT : Noise Power : {noise_power}")
print(f"FFT : SNR: {snr_fft}")









