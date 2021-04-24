

from SoundFontsData import SOUNDFONT_FILES, SOUNDFONT_SETTINGS


# use a library to render sample and load it?
class SoundFontInstrument(object):
    def __init__(self, nameInstrument: str, maxSample: int = 10):
        self.mNameInstrument = nameInstrument
        self.mSamples = {}
    def LoadSample(self, musistrataHeight: int):
        ### NOT IMPLEMENTED YET ###
        instrumentSettings = SOUNDFONT_SETTINGS[self.mNameInstrument]
        sfFile = SOUNDFONT_FILES[instrumentSettings["File"]]
        self.mSamples[musistrataHeight] = []
        raise(NotImplementedError)
    def __call__(self, musistrataHeight: int):
        if musistrataHeight not in self.mSamples.keys():
            self.LoadSample(musistrataHeight)
        return self.mSamples[musistrataHeight]




class SoundFontsLoader(object):
    def __init__(self, nbSamplesMaxPerInstrument: int = 10):
        self.mMaxSamples = nbSamplesMaxPerInstrument
        self.mInstruments = {}
    def __call__(self, instrumentName: str, musistrataHeight: int):
        return self.GetInstrument(instrumentName)(musistrataHeight)
    def GetInstrument(self, instrumentName: str):
        if instrumentName not in self.mInstruments.keys():
            self.mInstruments[instrumentName] = SoundFontInstrument(instrumentName)
        return self.mInstruments[instrumentName]





