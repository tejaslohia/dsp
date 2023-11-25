import numpy as np

def calculate_power(signal):
    return np.mean(np.square(signal))

# Example parameters
amplitude = 4.0
frequency = 50.0  # Hz
sampling_rate = 1024  # Hz
duration = 1.0  # seconds

# Generate a discrete sinusoidal signal
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
signal = amplitude * np.sin(2 * np.pi * frequency * t)

# Calculate the power of the signal
power = calculate_power(signal)

print(f"Power of the sinusoidal signal: {power}")

fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(fft_result), 1 / sampling_rate)

# Identify signal and noise components in the frequency domain
#signal_frequency_index = int(target_frequency * duration)
frequency_index = np.argmax(np.abs(fft_result))
#print(np.abs(fft_result))
#print(frequency_index)

amp=np.abs(fft_result[frequency_index])*2/len(fft_result)
print(amp)

fftPower = amp**2/2
print("fft power : ",fftPower)

