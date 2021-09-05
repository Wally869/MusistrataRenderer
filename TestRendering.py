

from MusiStrata import Song, Track, Bar, SoundEvent, Note
from Renderer import RenderSample, RenderTrack, RenderSong

from AudioUtils import WriteArrayToFile, PanStereoAudio, DelayStereoAudio


from simpleGen import testSong


def DoRender():
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
    #t = Track(Instrument="Stage_Grand_Piano", Bars=[b, b])
    t = Track(Instrument="SoundFont_Piano", Bars=[b, b])
    t2 = Track(Instrument="Acoustic_Guitar", Bars=[b2, b2])

    s = Song(Tempo=60, Tracks=[t, t2])
    TEMP_FOLDER = "Temp/"

    d = RenderTrack(t, 60)
    WriteArrayToFile(d, TEMP_FOLDER+"t1.wav")


if __name__ == "__main__":
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
    #t = Track(Instrument="Stage_Grand_Piano", Bars=[b, b])
    t = Track(Instrument="SoundFont_Piano", Bars=[b, b])
    t2 = Track(Instrument="Acoustic_Guitar", Bars=[b2, b2])

    s = Song(Tempo=60, Tracks=[t, t2])

    TEMP_FOLDER = "Temp/"

    d = RenderTrack(t, 60)
    WriteArrayToFile(d, TEMP_FOLDER+"t1.wav")

    d2 = RenderTrack(t, 180)
    WriteArrayToFile(d2, TEMP_FOLDER+"t2.wav")

    d3 = DelayStereoAudio(d, 0.5, 0.5)
    WriteArrayToFile(d3, TEMP_FOLDER+"delayed.wav")

    d4 = RenderSong(s)
    WriteArrayToFile(d4, TEMP_FOLDER+"s1.wav")

    d5 = RenderTrack(t, 60)
    d5 = PanStereoAudio(d5, 0.33)

    d6 = RenderTrack(t2, 60)
    d6 = PanStereoAudio(d6, 0.66)

    o1 = d5 + d6
    WriteArrayToFile(o1, TEMP_FOLDER+"s2.wav")

    so = RenderSong(testSong)
    WriteArrayToFile(so, TEMP_FOLDER+"testSong.wav")

