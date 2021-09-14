"""
    Contains the SoundFontsLoader and SoundFontInstrument classes, which handle loading and caching samples for Soundfont-based instruments.

"""

from typing import Dict

from SoundFontsData import SOUNDFONT_FILES, SOUNDFONT_SETTINGS
from SoundFontsDataController import SoundFontsDataController as sfdc

from MusiStrata.Components import Song, Track, Bar, SoundEvent, Note 
from MusiStrata import MidoConverter
from AudioUtils import PanMonoAudio

import Settings as SETTINGS

import librosa
import os

import numpy as np


# use a library to render sample and load it?
# should use this instead of midi2audio? https://github.com/nwhitehead/pyfluidsynth
class SoundFontInstrument(object):
    """
        Class handling loading of samples for a soundfont instrument
    """
    def __init__(self, nameInstrument: str, maxSample: int = 10):
        self.mNameInstrument = nameInstrument
        self.kSettings = sfdc.GetSettingsInstrument(nameInstrument)
        self.mSamples = {}

    def LoadSample(self, musistrataHeight: int) -> None:
        """
            Load a sample in memory. Calls self.GenerateSample if the sample has not been extracted from the soundfont
        """
        # Check if sample already generated, else generate it then load it
        fileName = self.mNameInstrument + "_" + str(musistrataHeight - 12) + ".wav"
        if (not os.path.exists(SETTINGS.SOUNDFONTS_SAMPLES_FOLDER + "/" + fileName)):
            self.GenerateSample(musistrataHeight)
        y, _ = librosa.load(SETTINGS.SOUNDFONTS_SAMPLES_FOLDER + "/" + fileName, sr=None, mono=True)
        # audio is mono, so panning to get stereo
        y = PanMonoAudio(y, 0.5)
        self.mSamples[musistrataHeight] = y

    def __call__(self, musistrataHeight: int) -> np.ndarray:
        """
            Get instrument sample for given height
        """
        if musistrataHeight not in self.mSamples.keys():
            self.LoadSample(musistrataHeight)
        return self.mSamples[musistrataHeight]

    def GenerateSample(self, musistrataHeight: int) -> None:
        """
            Extract sample from soundfont by calling self.GenerateMidi to generate a midi and rendering it to wav using fluidsynth + sox.  
        """
        baseFileName = self.mNameInstrument + "_" + str(musistrataHeight - 12)
        self.GenerateMidi(musistrataHeight)
        command_fluidsynth = "fluidsynth -T raw -F " + "Temp/temp " + SETTINGS.SOUNDFONTS_FOLDER + "/" + self.kSettings["File"] + " " + SETTINGS.TEMPORARY_MIDI_FOLDER + "/" + baseFileName + ".mid"
        command_sox = "sox -t raw -r 44100 -e signed -b 16 -c 1 -v 15 Temp/temp " + SETTINGS.SOUNDFONTS_SAMPLES_FOLDER + "/" + baseFileName + ".wav " + "speed 2"
        command = command_fluidsynth + " && " + command_sox
        os.system(command)

    def GenerateMidi(self, musistrataHeight: int) -> None:
        """
            Generate a midi for a single note using Musistrata and instrument settings.
        """
        n = Note.FromHeight(musistrataHeight)
        b = Bar([SoundEvent(0.0, SETTINGS.SOUNDFONT_SAMPLE_DURATION, n)])
        t = Track(Instrument=self.kSettings["SoundFontSettings"]["ChannelID"], BankUsed=self.kSettings["SoundFontSettings"]["BankID"], Bars=[b])
        s = Song(Tempo=60, BeatsPerBar=SETTINGS.SOUNDFONT_SAMPLE_DURATION, Tracks=[t])
        baseFileName = self.mNameInstrument + "_" + str(musistrataHeight - 12)
        MidoConverter.ConvertSong(s, SETTINGS.TEMPORARY_MIDI_FOLDER + "/" + baseFileName + ".mid")


class SoundFontsLoader(object):
    """
        Class handling loading and caching of soundfont-based instruments
    """
    def __init__(self, nbSamplesMaxPerInstrument: int = 10):
        self.mMaxSamples = nbSamplesMaxPerInstrument
        self.mInstruments = {}

    def __call__(self, instrumentName: str, musistrataHeight: int) -> np.ndarray:
        """
            Get sample for a named instrument at given height.
        """
        return self.GetInstrument(instrumentName)(musistrataHeight)

    def GetInstrument(self, instrumentName: str) -> SoundFontInstrument:
        """
            Get the SoundFontInstrument object associated to an instrument name.
        """
        if instrumentName not in self.mInstruments.keys():
            self.mInstruments[instrumentName] = SoundFontInstrument(instrumentName)
        return self.mInstruments[instrumentName]

    def GetSettingsInstrument(self, instrumentName: str) -> Dict:
        """
            Get settings associated with a given instrument name.
        """
        if instrumentName not in self.mInstruments.keys():
            self.mInstruments[instrumentName] = SoundFontInstrument(instrumentName)
        return self.mInstruments[instrumentName].kSettings["InstrumentSettings"]





