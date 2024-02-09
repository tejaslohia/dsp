#ubuntu record with two channel arecord test.wav -f S16_LE -c 2

from os.path import dirname, join as pjoin
from scipy.io import wavfile
import numpy as np
import scipy.io
from scipy import signal
from matplotlib import cm # colour map
from matplotlib import mlab

import os
print(os.getcwd())


import numpy as np

def specgram3d(y, srate=44100, ax=None, title=None):
  if not ax:
    ax = plt.axes(projection='3d')
  ax.set_title(title, loc='center', wrap=True)
  spec, freqs, t = mlab.specgram(y, Fs=srate)
  X, Y, Z = t[None, :], freqs[:, None],  20.0 * np.log10(spec)
  ax.plot_surface(X, Y, Z, cmap='viridis')
  ax.set_xlabel('time (s)')
  ax.set_ylabel('frequencies (Hz)')
  ax.set_zlabel('amplitude (dB)')
  ax.set_zlim(-140, 0)
  return X, Y, Z

wav_fname = './fft/test.wav'
#wav_fname = './test.wav'
samplerate, data = wavfile.read(wav_fname)
print(f"number of channels = {data.ndim}")
length = data.shape[0] / samplerate
print(f"length = {length}s")

import matplotlib.pyplot as plt
import numpy as np
time = np.linspace(0., length, data.shape[0])
plt.plot(time, data[:, 0], label="Left channel")
plt.plot(time, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

# extract the spectrum
startIndex=int(samplerate*0.0)
dd=data[startIndex:, 0]
#freq_bins, timestamps, spec = signal.spectrogram(data[:, 0], samplerate)
freq_bins, timestamps, spec = signal.spectrogram(dd, samplerate)

# 3d plot
fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.plot_surface(freq_bins[:, None], timestamps[None, :], 10.0*np.log10(spec), cmap=cm.coolwarm)
ax.plot_surface(freq_bins[:, None], timestamps[None, :], spec, cmap=cm.coolwarm)

#ax.plot_surface(timestamps[None, :],freq_bins[:, None], spec, cmap=cm.coolwarm)
ax.set_ylabel('time (s)')
ax.set_xlabel('frequencies (Hz)')
ax.set_zlabel('amplitude')
plt.show()
'''
y=spec

fig2, ax2 = plt.subplots(subplot_kw={'projection': '3d'})
specgram3d(y, srate=fs, title=title, ax=ax2)
'''