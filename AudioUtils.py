

import numpy as np


# using constant power pan: https://www.kvraudio.com/forum/viewtopic.php?t=148865 
# check this too: http://www.rs-met.com/documents/tutorials/PanRules.pdf
def PanStereoAudio(data: np.ndarray, panning: float) -> np.ndarray:
    output = np.zeros_like(data)
    output[0] = np.cos(panning * np.pi / 2) * data[0]
    output[1] = np.sin(panning * np.pi / 2) * data[1]
    return output


def PanMonoAudio(data: np.ndarray, panning: float) -> np.ndarray:
    outputData = np.zeros((2, len(data)))
    outputData[0, :] = np.cos(panning * np.pi / 2) * data[0]
    outputData[1, :] = np.sin(panning * np.pi / 2) * data[1]
    return outputData


def DelayMonoAudio(data: np.ndarray, lenDelay: float = 1.0, multiplierDelay: float = 0.5, sampleRate: int = 44100):
    output = np.zeros((1, int(len(data) + lenDelay * sampleRate)))
    output[:, :len(data)] = data
    output[:, int(lenDelay * sampleRate):] += data * multiplierDelay
    return output


def DelayStereoAudio(data: np.ndarray, lenDelay: float = 1.0, multiplierDelay: float = 0.5, sampleRate: int = 44100):
    output = np.zeros((2, int(len(data[0]) + lenDelay * sampleRate)))
    output[:, :len(data[0])] = data
    output[:, int(lenDelay * sampleRate):] += data * multiplierDelay
    return output

