import sounddevice as sd
import numpy as np

duration = 2.0
fs = 44100
t = np.linspace(0, duration, int(fs*duration), endpoint=False)
x = 0.1 * np.sin(2*np.pi*440*t)

sd.play(x, samplerate=fs, device=1)
sd.wait()
