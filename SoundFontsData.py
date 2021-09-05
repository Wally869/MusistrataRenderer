"""
    Settings for SoundFont files and SoundFont-based instruments. 

"""

# Soundfonts are not directly in a folder
# need to reference the soundfont file, the channel number and 
SOUNDFONT_INSTRUMENTS = [
    "SoundFont_Piano"

]


# Give soundfont name and path to file
SOUNDFONT_FILES = {
    "florestan": "florestan-subset.sf2",
    "gs": "gs.sf2"

}


SOUNDFONT_SETTINGS = {
    "SoundFont_Piano": {
        "File": "gs",
        "ChannelID": 0,
        "BankID": 2

    }
}

SOUNDFONT_INSTRUMENTS_SETTINGS = {
    "Default": {
        "Decay": 0.5
    },
    "SoundFont_Piano": {
        "Decay": 0.5
    }

}




