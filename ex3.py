'''
https://stackoverflow.com/questions/14058340/adding-noise-to-a-signal-in-python
'''
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(1, 100, 1000)
x_volts = 10*np.sin(t/(2*np.pi))
x_watts = x_volts ** 2
x_db = 10 * np.log10(x_watts)

# Adding noise using target SNR
# Adding noise using a target noise power

# Set a target channel noise power to something very noisy
target_noise_db = 10

# Convert to linear Watt units
target_noise_watts = 10 ** (target_noise_db / 10)

# Generate noise samples
mean_noise = 0
noise_volts = np.random.normal(mean_noise, np.sqrt(target_noise_watts), len(x_watts))

# Noise up the original signal (again) and plot
y_volts = x_volts + noise_volts

# Plot signal with noise
plt.subplot(2,1,1)
plt.plot(t, y_volts)
plt.title('Signal with noise')
plt.ylabel('Voltage (V)')
plt.xlabel('Time (s)')
#plt.show()
# Plot in dB
y_watts = y_volts ** 2
y_db = 10 * np.log10(y_watts)
plt.subplot(2,1,2)
plt.plot(t, 10* np.log10(y_volts**2))
plt.title('Signal with noise')
plt.ylabel('Power (dB)')
plt.xlabel('Time (s)')
plt.show()