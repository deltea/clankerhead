import sounddevice as sd
import numpy as np

mic_index = 2
duration = 2
fs = 44100

print("Recording...")
rec = sd.rec(int(duration*fs), samplerate=fs, channels=2, device=mic_index)
sd.wait()
print("Done. RMS:", np.sqrt(np.mean(rec**2)))
