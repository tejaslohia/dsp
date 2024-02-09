import numpy as np
import sounddevice as sd
import time

def play_note(frequency, duration):
    t = np.arange(int(44100 * duration)) / 44100
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, samplerate=44100)
    sd.wait()

# Define frequencies for notes
notes = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25,
         587.33, 659.26, 698.46, 783.99, 880.00, 987.77, 1046.50, 1174.66,
         1318.51, 1396.91, 1567.98, 1760.00, 1975.53, 2093.00, 0]

# Define durations for each note
durations = [4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4]

# Loop through the notes and play the anthem
for i in range(len(notes)):
    if notes[i] == 0:  # Rest
        time.sleep(durations[i] * 0.5)
    else:
        play_note(notes[i], durations[i] * 0.5)
        time.sleep(0.1)  # Add a short pause between notes
