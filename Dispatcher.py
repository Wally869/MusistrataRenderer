
from SoundFontsData import SOUNDFONT_INSTRUMENTS
from SoundFontsLoader import *

from SamplesData import SAMPLES_INSTRUMENTS
from SamplesLoader import *  

import Settings as SETTINGS

# call it something else than dispatcher I guess  
class Dispatcher(object):
    def __init__(self):
        self.mSoundFontsLoader = SoundFontsLoader(SETTINGS.NB_SAMPLES_STORED_PER_INSTRUMENT)
        self.mSamplesLoader = SamplesLoader(SETTINGS.NB_SAMPLES_STORED_PER_INSTRUMENT)
    def __call__(self, instrumentName: str, musistrataHeight: int):
        if instrumentName in SOUNDFONT_INSTRUMENTS:
            return self.mSoundFontsLoader(instrumentName, musistrataHeight)
        elif instrumentName in SAMPLES_INSTRUMENTS:
            return self.mSamplesLoader(instrumentName, musistrataHeight)
        else:
            raise("Dispatcher - Call -- Unknown Instrument")

