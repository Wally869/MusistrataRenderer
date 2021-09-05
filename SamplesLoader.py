"""
    Contains the SamplesLoader and SamplesInstrument classes, which handle loading and caching samples for Samples-based instruments.

"""

from typing import Dict

import librosa

from SamplesDataController import SamplesDataController as sdc
import Settings as SETTINGS

import numpy as np

class SamplesInstrument(object):
    """
        Class handling loading of samples for a samples-based instrument.
    """
    def __init__(self, nameInstrument: str, maxSample: int = 10):
        self.mNameInstrument = nameInstrument
        self.kSettings = sdc.GetSettingsInstrument(nameInstrument)
        self.mSamples = {}

    def LoadSample(self, musistrataHeight: int) -> None:
        """
            Load a sample in memory.
        """
        y, _ = librosa.load(SETTINGS.SAMPLES_FOLDER + "/" + self.kSettings["Folder"] + "/" + self.mNameInstrument + "_" + str(musistrataHeight - 12) + ".wav", sr=None, mono=False)
        self.mSamples[musistrataHeight] = y

    def __call__(self, musistrataHeight: int) -> np.ndarray:
        """
            Get instrument sample for given height
        """
        if musistrataHeight not in self.mSamples.keys():
            self.LoadSample(musistrataHeight)
        return self.mSamples[musistrataHeight]


class SamplesLoader(object):
    """
        Class handling loading and caching of samples-based instruments
    """
    def __init__(self, nbSamplesMaxPerInstrument: int = 10):
        self.mMaxSamples = nbSamplesMaxPerInstrument
        self.mInstruments = {}

    def __call__(self, instrumentName: str, musistrataHeight: int) -> np.ndarray:
        """
            Get sample for a named instrument at given height.
        """
        return self.GetInstrument(instrumentName)(musistrataHeight)

    def GetInstrument(self, instrumentName: str) -> SamplesInstrument:
        """
            Get the SamplesInstrument object associated to an instrument name.
        """
        if instrumentName not in self.mInstruments.keys():
            self.mInstruments[instrumentName] = SamplesInstrument(instrumentName)
        return self.mInstruments[instrumentName]

    def GetSettingsInstrument(self, instrumentName: str) -> Dict:
        """
            Get settings associated with a given instrument name.
        """
        if instrumentName not in self.mInstruments.keys():
            self.mInstruments[instrumentName] = SamplesInstrument(instrumentName)
        return self.mInstruments[instrumentName].kSettings["InstrumentSettings"]
