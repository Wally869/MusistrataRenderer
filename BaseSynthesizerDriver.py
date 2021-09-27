from typing import Dict

from AudioUtils import PanMonoAudio
import numpy as np

import Settings as SETTINGS 

class BaseSynthesizerDriver(object):
    def __init__(self, **kwargs) -> None:
        pass

    @classmethod
    def Generate(cls, frequency: float, payload: Dict) -> np.ndarray:
        deltaTimes = np.arange(SETTINGS.SOUNDFONT_SAMPLE_DURATION * SETTINGS.SAMPLE_RATE) / SETTINGS.SAMPLE_RATE
        y = np.zeros_like(deltaTimes)
        for expr in payload["expressions"]:
            y += expr["multiplier"] * eval(expr["expression"])
        y /= np.max(np.abs(y))
        y = PanMonoAudio(y, 0.5)
        return y  #/ np.max(y)



