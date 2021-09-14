"""
    Contains the SynthesizerLoader and SynthesizerInstrument classes, which handle loading and caching samples for synthesizer-based instruments.

"""

from typing import Dict


from SynthesizerDataController import SynthesizerDataController as sdc

from MusiStrata.Components import Song, Track, Bar, SoundEvent, Note 
from MusiStrata import MidoConverter
from AudioUtils import PanMonoAudio

import Settings as SETTINGS


import numpy as np


class SynthesizerInstrument(object):
    """
        Class handling loading of samples for a soundfont instrument
    """
    def __init__(self, nameInstrument: str, maxSample: int = 10):
        self.mNameInstrument = nameInstrument
        self.kSettings = sdc.GetSettingsInstrument(nameInstrument)
        self.mSamples = {}

    def LoadSample(self, musistrataHeight: int) -> None:
        """
            Load a sample in memory. Calls self.GenerateSample if the sample has not been extracted from the soundfont
        """
        # Check if sample already generated, else generate it then load it
        frequency = Note.FromHeight(musistrataHeight + 12).Frequency
        deltaTimes = np.arange(20.0 * 44100) / 44100
        y = np.sin(frequency * deltaTimes) * np.exp(-0.0015 * frequency * deltaTimes)
        y += 0.6 * np.sin(frequency * 2.0 * deltaTimes) * np.exp(-0.0015 * frequency * deltaTimes)
        y /= np.max(y)
        self.mSamples[musistrataHeight] = PanMonoAudio(y, 0.5)

    def __call__(self, musistrataHeight: int) -> np.ndarray:
        """
            Get instrument sample for given height
        """
        if musistrataHeight not in self.mSamples.keys():
            self.LoadSample(musistrataHeight)
        return self.mSamples[musistrataHeight]


class SynthesizerLoader(object):
    """
        Class handling loading and caching of synthesizer-based instruments
    """
    def __init__(self, nbSamplesMaxPerInstrument: int = 10):
        self.mMaxSamples = nbSamplesMaxPerInstrument
        self.mInstruments = {}

    def __call__(self, instrumentName: str, musistrataHeight: int) -> np.ndarray:
        """
            Get sample for a named instrument at given height.
        """
        return self.GetInstrument(instrumentName)(musistrataHeight)

    def GetInstrument(self, instrumentName: str) -> SynthesizerInstrument:
        """
            Get the SynthesizerInstrument object associated to an instrument name.
        """
        if instrumentName not in self.mInstruments.keys():
            self.mInstruments[instrumentName] = SynthesizerInstrument(instrumentName)
        return self.mInstruments[instrumentName]

    def GetSettingsInstrument(self, instrumentName: str) -> Dict:
        """
            Get settings associated with a given instrument name.
        """
        if instrumentName not in self.mInstruments.keys():
            self.mInstruments[instrumentName] = SynthesizerInstrument(instrumentName)
        return self.mInstruments[instrumentName].kSettings["InstrumentSettings"]





