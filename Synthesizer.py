


import numpy as np

from MusiStrata import Note

from Interfaces import ISynthesizer

class Synthesizer(object):
    def __init__(self):
        pass

    def Render(self, heightNote: int, duration: float, sampleRate: float) -> np.ndarray:
        frequency = Note.FromHeight(heightNote).Frequency
        deltaTimes = np.arange(duration * sampleRate) / sampleRate
        return np.sin(frequency * deltaTimes) * np.exp(-0.0015 * frequency * deltaTimes)

