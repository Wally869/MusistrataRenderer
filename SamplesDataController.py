"""
    Controller for Samples-based instrument settings. 

"""

from typing import Dict

from SamplesData import SAMPLES_INSTRUMENTS,SAMPLES_INSTRUMENTS_SETTINGS, SAMPLES_FOLDERS

class SamplesDataController(object):
    def __init__(self):
        pass

    @classmethod
    def GetSettingsInstrument(cls, nameInstrument: str) -> Dict:
        if nameInstrument not in SAMPLES_INSTRUMENTS_SETTINGS.keys():
            return {
                "Folder": SAMPLES_FOLDERS[nameInstrument],
                "InstrumentSettings": SAMPLES_INSTRUMENTS_SETTINGS["Default"]
            }
        else:
            return {
                "Folder": SAMPLES_FOLDERS[nameInstrument],
                "InstrumentSettings": SAMPLES_INSTRUMENTS_SETTINGS[nameInstrument]
            }

