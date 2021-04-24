import numpy as np
import librosa


# here assuming stereo
def RenderSample(targetDuration: float, decayDuration: float, sampleData: np.ndarray, sampleRate: int = 44100) -> np.ndarray:
    terminalIndex = int(targetDuration * sampleRate)
    decayTerminalIndex = int((targetDuration + decayDuration) * sampleRate)
    arr = np.zeros((2, decayTerminalIndex), dtype=float)
    arr[:, :decayTerminalIndex] = sampleData[:, :decayTerminalIndex]
    arr[:, terminalIndex:decayTerminalIndex] *= np.arange(decayTerminalIndex - terminalIndex)[::-1] / (decayTerminalIndex - terminalIndex)
    return arr

