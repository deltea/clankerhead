import numpy as np
import sounddevice as sd
import queue
import time

SAMPLE_RATE = 44100
CHANNELS = 2
BLOCK_SIZE = 1024
PITCH_SHIFT = 1.4
LED_MOUTH_LEVELS = 3

INPUT_DEVICE = 2
OUTPUT_DEVICE = 1

audio_q = queue.Queue()

def draw_mouth(level):
    # replace this with your actual LED matrix code
    shapes = ["CLOSED", "MID", "OPEN"]
    print(f"Mouth: {shapes[min(level, LED_MOUTH_LEVELS-1)]}", end="\r")

def pitch_shift_block(block, pitch):
    indices = np.round(np.arange(0, len(block), pitch))
    indices = indices[indices < len(block)].astype(int)
    shifted = block[indices]

    # resize to original block length
    if len(shifted) < len(block):
        # pad with zeros
        shifted = np.pad(shifted, (0, len(block) - len(shifted)))
    else:
        # truncate
        shifted = shifted[:len(block)]
    return shifted

def audio_callback(indata, outdata, frames, time_info, status):
    if status: print(status)

    # apply pitch shift per channel
    shifted = np.zeros_like(indata)
    for ch in range(CHANNELS):
        shifted[:, ch] = pitch_shift_block(indata[:, ch], PITCH_SHIFT)

    outdata[:] = shifted

    # compute rms amplitude for mouth
    rms = np.sqrt(np.mean(np.square(indata)))

    # change rms scaling to mouth
    level = int(min(rms * 10, LED_MOUTH_LEVELS - 1))
    draw_mouth(level)

with sd.Stream(
    channels=CHANNELS,
    samplerate=SAMPLE_RATE,
    blocksize=BLOCK_SIZE,
    device=(INPUT_DEVICE, OUTPUT_DEVICE),
    callback=audio_callback
):
    print("running voice changer + mouth. press ctrl+c to stop")
    while True:
        time.sleep(0.1)
