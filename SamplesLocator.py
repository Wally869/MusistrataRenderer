"""
    Contains the SampleLocator class, which routes samples loading queries between Soundfont-based instruments and Samples-based instruments.

"""


from typing import Dict

from SoundFontsData import SOUNDFONT_INSTRUMENTS
from SoundFontsLoader import SoundFontsLoader

from SamplesData import SAMPLES_INSTRUMENTS
from SamplesLoader import SamplesLoader  

from SynthesizerData import SYNTHESIZER_INSTRUMENTS
from SynthesizerLoader import SynthesizerLoader

import Settings as SETTINGS

import numpy as np

class SamplesLocator(object):
    """
        Handle locating instrument samples. Routes between Soundfont-based instruments and Samples-based instruments. 
    """
    def __init__(self):
        self.mSoundFontsLoader = SoundFontsLoader(SETTINGS.NB_SAMPLES_STORED_PER_INSTRUMENT)
        self.mSamplesLoader = SamplesLoader(SETTINGS.NB_SAMPLES_STORED_PER_INSTRUMENT)
        self.mSynthesizerLoader = SynthesizerLoader(SETTINGS.NB_SAMPLES_STORED_PER_INSTRUMENT)

    def __call__(self, instrumentName: str, musistrataHeight: int) -> np.ndarray:
        """
            Get sample for given instrument and height
        """
        if instrumentName in SOUNDFONT_INSTRUMENTS:
            return self.mSoundFontsLoader(instrumentName, musistrataHeight)
        elif instrumentName in SAMPLES_INSTRUMENTS:
            return self.mSamplesLoader(instrumentName, musistrataHeight)
        elif instrumentName in SYNTHESIZER_INSTRUMENTS:
            return self.mSynthesizerLoader(instrumentName, musistrataHeight)
        else:
            errorMessage = "SamplesLocator - Call -- Unknown Instrument (" + instrumentName + ")" 
            raise(KeyError(errorMessage))
        
    def GetSettingsInstrument(self, instrumentName: str) -> Dict:
        """
            Get instrument settings.
        """
        if instrumentName in SOUNDFONT_INSTRUMENTS:
            return self.mSoundFontsLoader.GetSettingsInstrument(instrumentName)
        elif instrumentName in SAMPLES_INSTRUMENTS:
            return self.mSamplesLoader.GetSettingsInstrument(instrumentName)
        elif instrumentName in SYNTHESIZER_INSTRUMENTS:
            return self.mSynthesizerLoader.GetSettingsInstrument(instrumentName)            
        else:
            errorMessage = "SamplesLocator - GetSettingsInstrument -- Unknown Instrument (" + instrumentName + ")"
            raise(KeyError(errorMessage))

