import numpy as np
import matplotlib.pyplot as plt

def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Parameters
Fs = 300e3        # Sampling frequency in Hz
Fc = 100e3        # Cutoff frequency in Hz
N = 20            # Number of samples for moving average

# Generate a sample signal (replace this with your actual signal)
t = np.arange(0, 0.001, 1/Fs)  # Time vector
signal = np.sin(2 * np.pi * 50e3 * t)  # Example: 50 kHz sine wave

# Apply the moving average filter
filtered_signal = moving_average(signal, N)

# Plot original and filtered signals
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
filtered_time = t[:len(filtered_signal)]  # Adjust time vector for filtered signal
plt.plot(filtered_time, filtered_signal)
plt.title('Filtered Signal (Moving Average)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()