

from MusiStrata import *

from SoundfontRenderer import *
from SamplesRenderer import *

from DispatcherData import * 

from SamplesLoader import *

from AudioUtils import *

import librosa
import numpy as np

PADDING_SECONDS = 2.0

PATH_SAMPLER = ""


class Dispatcher(object):
    def __init__(self):
        pass


def RenderTrack(track: Track, tempo: int, beatsPerBar: int = 4, decayDuration: float = 0.5, sampleRate: int = 44100, stereo: bool = True) -> np.ndarray:
    # Determine length
    duration = len(track.Bars) * beatsPerBar
    arr = np.zeros((2, int(duration * sampleRate * 60 / tempo + PADDING_SECONDS * sampleRate)))
    loader = Loader()
    for idBar, bar in enumerate(track.Bars):
        for _, soundEvent in enumerate(bar.SoundEvents):
            y = loader(track.Instrument, soundEvent.Note.Height)
            for i in range(2):
                initialIndex = int((idBar * beatsPerBar + soundEvent.Beat) * 60 / tempo * sampleRate) 
                terminalIndex = int((idBar * beatsPerBar + soundEvent.Beat + soundEvent.Duration) * 60 / tempo * sampleRate) 
                arr[i][initialIndex:terminalIndex] += y[i][:int(soundEvent.Duration * sampleRate * 60 / tempo)]
                decayIndex = terminalIndex + int(decayDuration * sampleRate)
                #print(len(y[i][int(soundEvent.Duration * sampleRate * 60 / tempo):int(soundEvent.Duration * sampleRate * 60 / tempo + decayDuration * sampleRate)]))
                arr[i][terminalIndex:decayIndex] += y[i][int(soundEvent.Duration * sampleRate * 60 / tempo):int(soundEvent.Duration * sampleRate * 60 / tempo + decayDuration * sampleRate)] * np.arange(len(arr[i][terminalIndex:decayIndex]))[::-1] / (len(arr[i][terminalIndex:decayIndex]))
    return arr


def RenderSong(song: Song, sampleRate: int = 44100) -> np.ndarray:
    tracks = []
    for track in song.Tracks:
        tracks.append(
            RenderTrack(track, song.Tempo, song.BeatsPerBar)
        )
    arr = tracks[0]
    for i in range(1, len(tracks)):
        arr += tracks[i]
    return arr



def WriteArrayToFile(data: np.ndarray, filename: str, sampleRate: int = 44100):
    librosa.output.write_wav(filename, np.asfortranarray(data), sampleRate)



se = [
    SoundEvent(0.0, 2.0, Note=Note("C", 5)),
    SoundEvent(1.0, 2.0, Note=Note("E", 5)),
    SoundEvent(2.0, 2.0, Note=Note("G", 5))

]

se2 = [
    SoundEvent(0.0, 2.0, Note=Note("E", 6)),
    SoundEvent(2.0, 2.0, Note=Note("C", 6))

]

b = Bar(se)
b2 = Bar(se2)
t = Track(Instrument="Stage_Grand_Piano", Bars=[b, b])
t2 = Track(Instrument="Acoustic_Guitar", Bars=[b2, b2])

s = Song(Tempo=60, Tracks=[t, t2])

d = RenderTrack(t, 60)
WriteArrayToFile(d, "t1.wav")

d2 = RenderTrack(t, 180)
WriteArrayToFile(d2, "t2.wav")

d3 = DelayStereoAudio(d, 0.5, 0.5)
WriteArrayToFile(d3, "delayed.wav")

d4 = RenderSong(s)
WriteArrayToFile(d4, "s1.wav")

d5 = RenderTrack(t, 60)
d5 = PanStereoAudio(d5, 0.33)

d6 = RenderTrack(t2, 60)
d6 = PanStereoAudio(d6, 0.66)

o1 = d5 + d6
WriteArrayToFile(o1, "s2.wav")