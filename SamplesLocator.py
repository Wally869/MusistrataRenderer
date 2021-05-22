from typing import Dict

from SoundFontsData import SOUNDFONT_INSTRUMENTS
from SoundFontsLoader import *

from SamplesData import SAMPLES_INSTRUMENTS
from SamplesLoader import *  

import Settings as SETTINGS

import numpy as np

class SamplesLocator(object):
    def __init__(self):
        self.mSoundFontsLoader = SoundFontsLoader(SETTINGS.NB_SAMPLES_STORED_PER_INSTRUMENT)
        self.mSamplesLoader = SamplesLoader(SETTINGS.NB_SAMPLES_STORED_PER_INSTRUMENT)

    def __call__(self, instrumentName: str, musistrataHeight: int) -> np.ndarray:
        if instrumentName in SOUNDFONT_INSTRUMENTS:
            return self.mSoundFontsLoader(instrumentName, musistrataHeight)
        elif instrumentName in SAMPLES_INSTRUMENTS:
            return self.mSamplesLoader(instrumentName, musistrataHeight)
        else:
            raise("SamplesLocator - Call -- Unknown Instrument (" + instrumentName + ")")
        
    def GetSettingsInstrument(self, instrumentName) -> Dict:
        if instrumentName in SOUNDFONT_INSTRUMENTS:
            return self.mSoundFontsLoader.GetSettingsInstrument(instrumentName)
        elif instrumentName in SAMPLES_INSTRUMENTS:
            return self.mSamplesLoader.GetSettingsInstrument(instrumentName)
        else:
            raise("SamplesLocator - GetSettingsInstrument -- Unknown Instrument (" + instrumentName + ")")
