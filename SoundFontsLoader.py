from typing import Dict

from SoundFontsData import SOUNDFONT_FILES, SOUNDFONT_SETTINGS
from SoundFontsDataController import SoundFontsDataController as sfdc

from MusiStrata.Components import Song, Track, Bar, SoundEvent, Note 
from MusiStrata import MidoConverter
from AudioUtils import PanMonoAudio

import Settings as SETTINGS

import librosa
import os


# use a library to render sample and load it?
# should use this instead of midi2audio? https://github.com/nwhitehead/pyfluidsynth
class SoundFontInstrument(object):
    def __init__(self, nameInstrument: str, maxSample: int = 10):
        self.mNameInstrument = nameInstrument
        self.kSettings = sfdc.GetSettingsInstrument(nameInstrument)
        self.mSamples = {}

    def LoadSample(self, musistrataHeight: int):
        # Check if sample already generated, else generate it then load it
        fileName = self.mNameInstrument + "_" + str(musistrataHeight - 12) + ".wav"
        if (not os.path.exists(SETTINGS.SOUNDFONTS_SAMPLES_FOLDER + "/" + fileName)):
            self.GenerateSample(musistrataHeight)
        y, _ = librosa.load(SETTINGS.SOUNDFONTS_SAMPLES_FOLDER + "/" + fileName, sr=None, mono=True)
        # audio is mono, so panning to get stereo
        y = PanMonoAudio(y, 0.5)
        self.mSamples[musistrataHeight] = y

    def __call__(self, musistrataHeight: int):
        if musistrataHeight not in self.mSamples.keys():
            self.LoadSample(musistrataHeight)
        return self.mSamples[musistrataHeight]

    def GenerateSample(self, musistrataHeight: int):
        baseFileName = self.mNameInstrument + "_" + str(musistrataHeight - 12)
        self.GenerateMidi(musistrataHeight)
        command_fluidsynth = "fluidsynth -T raw -F " + "Temp/temp " + SETTINGS.SOUNDFONTS_FOLDER + "/" + self.kSettings["File"] + " " + SETTINGS.TEMPORARY_MIDI_FOLDER + "/" + baseFileName + ".mid"
        command_sox = "sox -t raw -r 44100 -e signed -b 16 -c 1 -v 15 Temp/temp " + SETTINGS.SOUNDFONTS_SAMPLES_FOLDER + "/" + baseFileName + ".wav " + "speed 2"
        command = command_fluidsynth + " && " + command_sox
        os.system(command)

    def GenerateMidi(self, musistrataHeight: int):
        n = Note.FromHeight(musistrataHeight)
        b = Bar([SoundEvent(0.0, SETTINGS.SOUNDFONT_SAMPLE_DURATION, n)])
        t = Track(Instrument=self.kSettings["SoundFontSettings"]["ChannelID"], BankUsed=self.kSettings["SoundFontSettings"]["BankID"], Bars=[b])
        s = Song(Tempo=60, BeatsPerBar=SETTINGS.SOUNDFONT_SAMPLE_DURATION, Tracks=[t])
        baseFileName = self.mNameInstrument + "_" + str(musistrataHeight - 12)
        MidoConverter.ConvertSong(s, SETTINGS.TEMPORARY_MIDI_FOLDER + "/" + baseFileName + ".mid")


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

    def GetSettingsInstrument(self, instrumentName: str) -> Dict:
        if instrumentName not in self.mInstruments.keys():
            self.mInstruments[instrumentName] = SoundFontInstrument(instrumentName)
        return self.mInstruments[instrumentName].kSettings["InstrumentSettings"]





