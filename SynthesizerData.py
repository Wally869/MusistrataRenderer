"""
    Definition of available synthesizer-based instruments. 

"""


SYNTHESIZER_INSTRUMENTS = [
    "Default_Synth",
    "test_synth"

]





SYNTHESIZER_INSTRUMENTS_SETTINGS = {
    "Default": {
        "Decay": 0.5
    }

}


SYNTHESIZER_INSTRUMENTS_PAYLOADS = {
    "Default_Synth": {
        "expressions": [
            {
                "expression": "np.sin(frequency * deltaTimes)",
                "multiplier": 1.0
            }

        ]
    },
    "test_synth": {
        "expressions": [
            {
                "expression": "np.sin(frequency * deltaTimes + np.sin(20 * deltaTimes)) * np.exp(-0.0015 * frequency * deltaTimes)",
                "multiplier": 1.0
            }, {
                "expression": "np.sin(2.0 * frequency * deltaTimes) * np.exp(-0.0015 * frequency * deltaTimes)",
                "multiplier": 0.6
            }
        ]
    }


}