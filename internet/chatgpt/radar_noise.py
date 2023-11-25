import numpy as np
import matplotlib.pyplot as plt

def generate_radar_signal(sampling_rate, duration, target_frequency, snr):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    
    # Generate a radar signal with a target frequency
    radar_signal = 5*np.sin(2 * np.pi * target_frequency * t)
    
    # Add noise to the signal
    noise = np.random.normal(0, 1, len(t))
    noise_power = np.sqrt(np.mean(noise**2))
    print(len(t))
    
    # Adjust noise amplitude to achieve the desired SNR
    radar_signal_power = np.sqrt(np.mean(radar_signal**2))
    noise_amplitude = radar_signal_power / (10**(snr / 20))
    noisy_signal = radar_signal + noise_amplitude * noise
    
    return t, noisy_signal, radar_signal, noise_amplitude * noise

def calculate_snr(signal, noise):
    signal_power = np.sum(np.abs(signal)**2)
    noise_power = np.sum(np.abs(noise)**2)
    
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

def main():
    # Parameters
    sampling_rate = 1000  # Hz
    duration = 1  # seconds
    target_frequency = 50  # Hz
    snr_target = 20  # dB

    # Generate radar signal with noise
    t, noisy_signal, radar_signal, noise = generate_radar_signal(sampling_rate, duration, target_frequency, snr_target)

    # Perform FFT on the received signal
    fft_result = np.fft.fft(noisy_signal)
    frequencies = np.fft.fftfreq(len(fft_result), 1 / sampling_rate)

    # Identify signal and noise components in the frequency domain
    signal_frequency_index = int(target_frequency * duration)
    noise_frequency_index = np.argmax(np.abs(fft_result))
    print(np.abs(fft_result))

    print(signal_frequency_index,noise_frequency_index)

    # Calculate SNR
    snr_result = calculate_snr(fft_result[signal_frequency_index], fft_result[noise_frequency_index])
    
    # Plot the radar signal, noise, and FFT results
    plt.subplot(3, 1, 1)
    plt.plot(t, noisy_signal, label='Noisy Signal')
    plt.plot(t, radar_signal, label='Radar Signal', linestyle='--')
    plt.legend()
    plt.title('Radar Signal with Noise')

    plt.subplot(3, 1, 2)
    plt.plot(t, noise, label='Noise')
    plt.legend()
    plt.title('Noise Component')

    plt.subplot(3, 1, 3)
    plt.plot(frequencies, np.abs(fft_result))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Frequency Domain Representation')
    plt.tight_layout()

    plt.show()

    print(f"SNR: {snr_result:.2f} dB")

if __name__ == "__main__":
    main()
