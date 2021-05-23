

from MusiStrata.Components import Song, Track, Bar, SoundEvent, Note
from MusiStrata import ScaleSpecs
from MusiStrata import MidoConverter

from random import choice

beatsPerBar = 4.0
tempo = 120.0

scaleNote = "C"
scaleMode = "Major"

scale = ScaleSpecs(scaleNote, scaleMode)
notes = scale.GetScaleNotes(5)
chords = scale.GetScaleChordsNotes()
chordos = scale.GetScaleChordsProgression()

# define a bass
# one note every bar that lasts the entire bar
# we'll do 8 bars
bassTones = [0, 2, 4, 3, 1, 1, 5, 6]



t = Track()
for idTone in range(len(bassTones)):
    c_notes = chords[bassTones[idTone]]
    b = Bar()
    for c in c_notes:
        b.SoundEvents.append(SoundEvent(0.0, beatsPerBar, c))
    t.Bars.append(b)

t.Instrument = "Acoustic_Guitar"


t2 = Track()
for idTone in range(len(bassTones)):
    c_notes = chords[bassTones[idTone]]
    c = notes[bassTones[idTone]] + 12
    c = choice(c_notes) + 12
    b = Bar([SoundEvent(0.0, beatsPerBar / 2, c)])
    c = choice(c_notes) + 12
    b.SoundEvents.append(SoundEvent(beatsPerBar/2, beatsPerBar / 2, c))
    t2.Bars.append(b)


t2.Instrument = "Close_Grand_Piano"

testSong = Song(Tempo=tempo, BeatsPerBar=beatsPerBar, Tracks=[t, t2])
MidoConverter.ConvertSong(testSong, "testSong.mid")


