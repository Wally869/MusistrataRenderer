from typing import Dict

from SoundFontsData import SOUNDFONT_FILES, SOUNDFONT_INSTRUMENTS, SOUNDFONT_INSTRUMENTS_SETTINGS, SOUNDFONT_SETTINGS

class SoundFontsDataController(object):
    def __init__(self):
        pass

    @classmethod
    def GetSettingsInstrument(cls, nameInstrument: str) -> Dict:
        if nameInstrument not in SOUNDFONT_INSTRUMENTS_SETTINGS.keys():
            return {
                "File": SOUNDFONT_FILES[SOUNDFONT_SETTINGS[nameInstrument]["File"]],
                "SoundFontSettings": SOUNDFONT_SETTINGS[nameInstrument],
                "InstrumentSettings": SOUNDFONT_INSTRUMENTS_SETTINGS["Default"]
            }
        else:
            return {
                "File": SOUNDFONT_FILES[SOUNDFONT_SETTINGS[nameInstrument]["File"]],
                "SoundFontSettings": SOUNDFONT_SETTINGS[nameInstrument],
                "InstrumentSettings": SOUNDFONT_INSTRUMENTS_SETTINGS[nameInstrument]
            }

