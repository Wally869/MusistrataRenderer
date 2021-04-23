

from MusiStrata import *

import numpy as np  

import librosa

# MusiStrata note is note.Height - 12 to get equivalent renderidoo?



FILE_SOUND = "Crystal_Keys/Crystal_Keys_51.wav"

FILE_SOUND_BASE = "Crystal_Keys/Crystal_Keys_"


se = [
    SoundEvent(0.0, 2.0, Note=Note("C", 5)),
    SoundEvent(1.0, 2.0, Note=Note("E", 5)),
    SoundEvent(2.0, 2.0, Note=Note("G", 5))

]


# compute full duration
duration = 0
for elem in se:
    if elem.Duration + elem.Beat > duration:
        duration = elem.Duration + elem.Beat

duration += 2  #padding

tempo = 60

sr = 44100
arr = np.zeros((2, int(duration * sr * 60 / tempo)))



for elem in se:
    y, _ = librosa.load(FILE_SOUND_BASE + str(elem.Note.Height - 12) + ".wav", sr=None, mono=False)
    for i in range(2):
        arr[i][int(elem.Beat * sr):int((elem.Beat + elem.Duration) * sr)] += y[i][:int(elem.Duration * sr)]

# supposedly deprecated, so will have to fix
# https://librosa.org/doc/0.7.2/generated/librosa.output.write_wav.html
librosa.output.write_wav("test.wav", np.asfortranarray(arr), sr)

# check to import wav as stereo file. Possibly librosa or will have to do my own parser


# Then parse the MusiStrata file. Or will use midi? For now can placeholder from json I guess


# Generate each track individually, and output a stereo wav file


# Apply mastering to each track


# Render all files to a single track


# Apply mastering to the whole
