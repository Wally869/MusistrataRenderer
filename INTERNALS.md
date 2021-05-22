# Internals  

The aim is to provide a unified interface to different sources of sounds/samples (sf2, wav, sfz... hopefully a custom python synth and VST).  
The approach I took is to create sample files in wav and load them in memory, to then write them to a numpy array (a track being the accumulation of all the notes from a given instrument, and a song the accumulation of all the tracks).   

But more than that, the loaders from different sources are separated and there is no problem with adding new sources once they are developped. 

All samples will have their amplitude remapped to the interval [-1, 1] so that there is no need to fiddle with gain for a given instrument: the Velocity defined in the MusiStrata file being used will define the actual amplitude of the sample in the song (we'll be using a 0-100 Velocity value).  

All instruments are referred by their names, and the appropriate lookup methods will return the sample for a note at a given height. All the complexity will be hidden from the user but will still allow him to add some customization. Most notably it is possible to set a custom Decay duration value to the instrument instead of the default (0.5).





