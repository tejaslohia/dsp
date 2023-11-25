import numpy as np
import matplotlib.pyplot as plt

def calculate_power(signal):
    magnitude_squared = np.abs(signal)**2
    average_power = np.mean(magnitude_squared)
    return average_power

def generate_radar_signal(sampling_rate, duration, target_frequency, snr):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    
    # Generate a radar signal with a target frequency
    radar_signal = 5*np.sin(2 * np.pi * target_frequency * t)
    
    # Add noise to the signal
    noise = np.random.normal(0, 1, len(t))
    #noise_power = np.sqrt(np.mean(noise**2))
    #print(len(t))
    
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
    snr_target = 10  # dB

    # Generate radar signal with noise
    t, noisy_signal, radar_signal, noise = generate_radar_signal(sampling_rate, duration, target_frequency, snr_target)

    radar_signal_power = calculate_power(radar_signal)
    noise_signal_power = calculate_power(noisy_signal)
    snr = 10 * np.log10(radar_signal_power/(noise_signal_power-radar_signal_power))
    print("noise raw poer",calculate_power(noise))
    print(f"radar power {radar_signal_power}")
    print(f"noise+radar power {noise_signal_power}")
    print(f"noise  power {noise_signal_power - radar_signal_power}")
    print(f"SNR {snr}")

    # Perform FFT on the received signal
    sigFFT=np.fft.fft(noisy_signal)
    fftLen=len(sigFFT)
    #normalizing sigFFT
    sigFFT=np.abs(sigFFT*2/fftLen)

    #normalized half sinnal
    sigFFTHalf=sigFFT[range((int)(fftLen/2))]

    #plot singal
   # plt.figure(figsize=(10, 6))
   # plt.plot(sigFFTHalf)
   # plt.show()
    #calculate power of total signal
    power=np.sum(sigFFTHalf**2/2)
    print("fft total power ",power)

    #calculate power of orig signal
    frequency_index = np.argmax(sigFFTHalf)
    signalAmp = sigFFTHalf[frequency_index]
    signal_power=signalAmp**2/2
    noise_power=power-signal_power
    snr_fft=10*np.log10(signal_power/noise_power)
    print(f"FFT : singal power: {signal_power}")
    print(f"FFT : noise power: {noise_power}")
    print(f"FFT : SNR: {snr_fft}")

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
    plt.plot(sigFFTHalf)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Frequency Domain Representation')
    plt.tight_layout()

    plt.show()

#    print(f"SNR: {snr_result:.2f} dB")

if __name__ == "__main__":
    main()
