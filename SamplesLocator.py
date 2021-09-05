"""
    Contains the SampleLocator class, which routes samples loading queries between Soundfont-based instruments and Samples-based instruments.

"""


from typing import Dict

from SoundFontsData import SOUNDFONT_INSTRUMENTS
from SoundFontsLoader import SoundFontsLoader

from SamplesData import SAMPLES_INSTRUMENTS
from SamplesLoader import SamplesLoader  

import Settings as SETTINGS

import numpy as np

class SamplesLocator(object):
    """
        Handle locating instrument samples. Routes between Soundfont-based instruments and Samples-based instruments. 
    """
    def __init__(self):
        self.mSoundFontsLoader = SoundFontsLoader(SETTINGS.NB_SAMPLES_STORED_PER_INSTRUMENT)
        self.mSamplesLoader = SamplesLoader(SETTINGS.NB_SAMPLES_STORED_PER_INSTRUMENT)

    def __call__(self, instrumentName: str, musistrataHeight: int) -> np.ndarray:
        """
            Get sample for given instrument and height
        """
        if instrumentName in SOUNDFONT_INSTRUMENTS:
            return self.mSoundFontsLoader(instrumentName, musistrataHeight)
        elif instrumentName in SAMPLES_INSTRUMENTS:
            return self.mSamplesLoader(instrumentName, musistrataHeight)
        else:
            raise("SamplesLocator - Call -- Unknown Instrument (" + instrumentName + ")")
        
    def GetSettingsInstrument(self, instrumentName: str) -> Dict:
        """
            Get instrument settings.
        """
        if instrumentName in SOUNDFONT_INSTRUMENTS:
            return self.mSoundFontsLoader.GetSettingsInstrument(instrumentName)
        elif instrumentName in SAMPLES_INSTRUMENTS:
            return self.mSamplesLoader.GetSettingsInstrument(instrumentName)
        else:
            raise("SamplesLocator - GetSettingsInstrument -- Unknown Instrument (" + instrumentName + ")")
