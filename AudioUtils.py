"""
    Utils to transform numpy arrays of sound signals:
    - Effects (panning, delay...)
    - Normalisation  
    - Writing to file
"""

import numpy as np
import soundfile


# using constant power pan: https://www.kvraudio.com/forum/viewtopic.php?t=148865 
# check this too: http://www.rs-met.com/documents/tutorials/PanRules.pdf
def PanStereoAudio(data: np.ndarray, panning: float) -> np.ndarray:
    """
        Takes a stereo signal and returns a panned stereo signal as a numpy array.
    """
    output = np.zeros_like(data)
    output[0] = np.cos(panning * np.pi / 2) * data[0]
    output[1] = np.sin(panning * np.pi / 2) * data[1]
    return output


def PanMonoAudio(data: np.ndarray, panning: float) -> np.ndarray:
    """
        Takes a mono signal and returns a panned stereo signal as a numpy array.
    """
    outputData = np.zeros((2, len(data)))
    outputData[0, :] = np.cos(panning * np.pi / 2) * data
    outputData[1, :] = np.sin(panning * np.pi / 2) * data
    return outputData


def DelayMonoAudio(data: np.ndarray, lenDelay: float = 1.0, multiplierDelay: float = 0.5, sampleRate: int = 44100) -> np.ndarray:
    """
        Takes a mono signal and returns a mono signal with added delay
    """
    output = np.zeros((1, int(len(data) + lenDelay * sampleRate)))
    output[:, :len(data)] = data
    output[:, int(lenDelay * sampleRate):] += data * multiplierDelay
    return output


def DelayStereoAudio(data: np.ndarray, lenDelay: float = 1.0, multiplierDelay: float = 0.5, sampleRate: int = 44100) -> np.ndarray:
    """
        Takes a stereo signal and returns a stereo signal with added delay
    """
    output = np.zeros((2, int(len(data[0]) + lenDelay * sampleRate)))
    output[:, :len(data[0])] = data
    output[:, int(lenDelay * sampleRate):] += data * multiplierDelay
    return output


def NormalizeAudio(data: np.ndarray) -> np.ndarray:
    """
        Normalizes an audio signal to [0; 1].
    """
    return data / np.max(np.abs(data))


def WriteArrayToFile(data: np.ndarray, filename: str, sampleRate: int = 44100) -> None:
    """
        Write a numpy array to a wav file.
    """
    soundfile.write(filename, data.T, sampleRate, "PCM_24")

