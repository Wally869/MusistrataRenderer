


from MusiStrata import * 

import json


# Using the generate example from package   
# to create a json representation of a musistrata song     
def GenerateExample1():
    note1 = SoundEvent(
        Beat=0.0,
        Duration=1.0,
        Note=Note(
            Name="A",
            Octave=5,
        )
    )
    note2 = SoundEvent(
        Beat=2.0,
        Duration=1.0,
        Note=Note(
            Name="C",
            Octave=5,
        )
    )
    note3 = SoundEvent(
        Beat=3.0,
        Duration=0.5,
        Note=Note(
            Name="D",
            Octave=5,
        )
    )
    bar = Bar(
        SoundEvents=[note1, note2, note3]
    )
    track = Track(
        Name="Main",
        Instrument="Vibraphone",
        Bars=[bar],
        BankUsed=1
    )
    song = Song(
        Tracks=[track]
    )
    return song


s = GenerateExample1()

MidoConverter.ConvertSong(s, "sampleFile.mid")
with open("sampleFile.json", "w") as f:
    json.dump(json.loads(s.ToJSON()), f)
