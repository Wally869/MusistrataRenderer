"""
    General Settings:  
        - Data Folders paths
        - Memory and Caching Settings
        - Rendering Settings

"""


# Loaders Settings
# Pathing
SAMPLES_FOLDER = "Samples"
SOUNDFONTS_FOLDER = "SoundFonts"
SOUNDFONTS_SAMPLES_FOLDER = "SoundFontsSamples"
TEMPORARY_MIDI_FOLDER = "MidiTemp"


# Memory Management
NB_SAMPLES_STORED_PER_INSTRUMENT = 10
CLEAR_SOUNDFONTS_MIDI_ON_EXIT = True
CLEAR_SOUNDFONTS_SAMPLES_ON_EXIT = False


# Rendering Settings
SOUNDFONT_SAMPLE_DURATION = 20.0  # in Seconds
SONG_PADDING_SECONDS = 2.0
SAMPLE_RATE = 44100  

