"""
    Controller for Synthesizer-based instrument settings. 

"""

from typing import Dict

from SynthesizerData import SYNTHESIZER_INSTRUMENTS, SYNTHESIZER_INSTRUMENTS_SETTINGS

class SynthesizerDataController(object):
    def __init__(self):
        pass
    
    @classmethod
    def GetSettingsInstrument(cls, nameInstrument: str) -> Dict:
        """
            Handle settings reading of Synthesizer-based instruments.
        """
        if nameInstrument not in SYNTHESIZER_INSTRUMENTS_SETTINGS.keys():
            return {
                "InstrumentSettings": SYNTHESIZER_INSTRUMENTS_SETTINGS["Default"]
            }
        else:
            return {
                "InstrumentSettings": SYNTHESIZER_INSTRUMENTS_SETTINGS[nameInstrument]
            }

