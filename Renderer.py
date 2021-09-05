"""
    Render MusiStrata songs and tracks to numpy array.  
"""

from MusiStrata.Components import Song, Track, Bar, SoundEvent, Note
from SamplesLocator import SamplesLocator

import numpy as np
import librosa

import Settings as SETTINGS


LOCATOR = SamplesLocator()


# here assuming stereo
def RenderSample(targetDuration: float, decayDuration: float, sampleData: np.ndarray, sampleRate: int = 44100) -> np.ndarray:
    """
        Render a sample to a target length with added decay.  
    """
    terminalIndex = int(targetDuration * sampleRate)
    decayTerminalIndex = int((targetDuration + decayDuration) * sampleRate)
    arr = np.zeros((2, decayTerminalIndex), dtype=float)
    arr[:, :decayTerminalIndex] = sampleData[:, :decayTerminalIndex]
    arr[:, terminalIndex:decayTerminalIndex] *= np.arange(decayTerminalIndex - terminalIndex)[::-1] / (decayTerminalIndex - terminalIndex)
    return arr


def RenderTrack(track: Track, tempo: int, beatsPerBar: int = 4, sampleRate: int = 44100, stereo: bool = True) -> np.ndarray:
    """
        Render a Musistrata track by reading all sound events, loading samples and writing to a numpy array.  
    """
    # Determine length
    duration = len(track.Bars) * beatsPerBar
    arr = np.zeros((2, int(duration * sampleRate * 60 / tempo + SETTINGS.SONG_PADDING_SECONDS * sampleRate)))
    for idBar, bar in enumerate(track.Bars):
        for _, soundEvent in enumerate(bar.SoundEvents):
            y = LOCATOR(track.Instrument, soundEvent.Note.Height)
            initialIndex = int((idBar * beatsPerBar + soundEvent.Beat) * 60 / tempo * sampleRate) 
            rendered = RenderSample(soundEvent.Duration * 60 / tempo,  LOCATOR.GetSettingsInstrument(track.Instrument)["Decay"], y) * soundEvent.Velocity / 100
            arr[:, initialIndex:(rendered.shape[1] + initialIndex)] += rendered  # directly using rendered shape: avoid potential rounding errors? Also good if adding effects?
    return arr


def RenderSong(song: Song, sampleRate: int = 44100) -> np.ndarray:
    """
        Render a Musistrata Song to a numpy array by rendering every track of the song to a different array, before summing these individual arrays.
    """
    tracks = []
    for track in song.Tracks:
        tracks.append(
            RenderTrack(track, song.Tempo, song.BeatsPerBar)
        )
    arr = tracks[0]
    for i in range(1, len(tracks)):
        arr += tracks[i]
    return arr
