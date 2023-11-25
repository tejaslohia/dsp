import numpy as np

signal=np.array([1,-3,4])

sum=np.sum(np.abs(signal)**2)
print(signal)
print(sum)

fft_result = np.fft.fft(noisy_signal)
frequencies = np.fft.fftfreq(len(fft_result), 1 / sampling_rate)

# Identify signal and noise components in the frequency domain
signal_frequency_index = int(target_frequency * duration)
noise_frequency_index = np.argmax(np.abs(fft_result))
print(np.abs(fft_result))