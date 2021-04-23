


import librosa


DEFAULT_SAMPLES_FOLDER = "Samples"

class InstrumentLoader(object):
    def __init__(self, nameInstrument: str, maxSample: int = 10):
        self.mNameInstrument = nameInstrument
        self.mSamples = {}
    def LoadSample(self, musistrataHeight: int):
        y, _ = librosa.load(DEFAULT_SAMPLES_FOLDER + "/" + self.mNameInstrument + "/" + self.mNameInstrument + "_" + str(musistrataHeight - 12) + ".wav", sr=None, mono=False)
        self.mSamples[musistrataHeight] = y
    def __call__(self, musistrataHeight: int):
        if musistrataHeight not in self.mSamples.keys():
            self.LoadSample(musistrataHeight)
        return self.mSamples[musistrataHeight]



class Loader(object):
    def __init__(self, nbSamplesMaxPerInstrument: int = 10):
        self.mMaxSamples = nbSamplesMaxPerInstrument
        self.mInstruments = {}
    def __call__(self, instrumentName: str, musistrataHeight: int):
        return self.GetInstrument(instrumentName)(musistrataHeight)
    def GetInstrument(self, instrumentName: str):
        if instrumentName not in self.mInstruments.keys():
            self.mInstruments[instrumentName] = InstrumentLoader(instrumentName)
        return self.mInstruments[instrumentName]
