import numpy as np
import sounddevice as sd

def calculate_rms(data):
    return np.sqrt(np.mean(np.square(data)))

def calculate_decibel(rms_value, reference=1.0):
    return 20 * np.log10(rms_value / reference)

def sound_level_callback(indata, frames, time, status):
    if status:
        print(f"Error in callback: {status}")
    rms_value = calculate_rms(indata)
    decibel_level = calculate_decibel(rms_value)
    print(f"Sound Level (dB): {decibel_level:.2f}")

# Set the sample rate and duration for recording
sample_rate = 44100  # You can adjust this based on your microphone specifications
duration = 5  # Recording duration in seconds

# Capture audio and calculate decibel level
with sd.InputStream(callback=sound_level_callback, channels=1, samplerate=sample_rate):
    print(f"Recording for {duration} seconds...")
    sd.sleep(int(duration * 1000))  # Sleep for the specified duration
    print("Recording complete.")
