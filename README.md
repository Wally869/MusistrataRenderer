# Musistrata Renderer  

Creating an interface to render Musistrata-defined songs using a variety of sources (soundfonts, user-defined samples, custom synthesizer...)  


## Why?  

DAWs do not allow for direct scripting/control over their engines and their file formats are proprietary and undocumented. VSTs Hosts are a mess (compatibility issues between 2.0 and 3.0), and usually encrypt their data. SF2 are low quality, or need heavy mastering as well as a variety of tools for rendering (FluidSynth & Sox) with some issues (the Fluidsynth version distributed on VCPKG is not the latest build and suffers a type error which prevents the use of soundfonts bigger than ~2gb).  
UPDATE: FluidSynth now distributes v2.2 binaries for Windows directly from github since 3 weeks ago, so this is not an issue anymore (https://github.com/FluidSynth/fluidsynth/releases/tag/v2.2.0)   


Since I wanted a fully automated pipeline to create songs and considering how fractured the musical production environment seems to be, I thought it easier to try to create a simple interface which would hide all the complexity.  

This is basically a sampler meant to interface with different sources and to be used to generate audio in a non-realtime fashion. By using a generator outputting a MusiStrata song, tracks are rendered seperately and can then be mastered and combined together to produce the final rendered song (see simpleGen.py and TestRendering.py).   


## Current  

Can load samples from a Samples folder (handled in samples loader file), or from a soundfont. Soundfont imports need to create an intermediary midi file, then create a wav file which is then read. Current setup uses MusiStrata to create a midi file, which is then rendered to RAW by fluidsynth and then to wav by SOX. Bit convoluted but I had issues with rendering midi to wav with fluidsynth on windows for some reason. Plus the conversion process would make FluidSynth play the sounds and would block execution while doing it, so using the raw format allowed to avoid this problem. Not sure if can fix, will check it out.  


AudioUtils.py contains some functions to add panning and delay to audio input. Careful: We use constant power panning, so I believe a panning of 0.5 (i.e. panned to the center) will result in a slight decrease in volume (lower sound amplitude). Will check it out.    

Renderer.py contains the functions responsible to render the MusiStrata.Track and MusiStrata.Song objects

## How to Use  

If using Samples:  
- Add wav samples to a named folder in the Samples directory   
- Add the instrument name and the folder's name to the dicts SamplesData.py  
- (Optional) add a custom decay duration for the instrument, also in SamplesData.py  

If using Soundfont instrument:  
- Put your soundfont file in the SoundFonts folder 
- In SoundFontsData.py, add all the information required to use the instrument. You'll need to add a Name for the instrument, the soundfont file name and path, and the lookup settings for the instrument (which soundfont file it uses, the channel ID and the bank used).  

Once all the setup has been done, you just need to use a MusiStrata Song, or Track, as input to the renderer.  

The rendering process is shown in TestRendering.py:  
- Tracks can be rendered seperately using the RenderTrack function, and Songs using the RenderSong function  
- Once rendered, it is possible to apply mastering effects to the rendered object (panning and delay only available for now) 
- The arrays containing the rendered sounds can be written to file using the WriteArrayToFile function from AudioUtils.py  

Most of the work to be done to use this library is in specifying the instruments settings. The SamplesLocator provides the single point of interfacing between the user and the library, and handles communication with the SamplesLoader and SoundFontsLoader classes.   


To Note:   
Instrument lookup is done by name so do your best to avoid name collisions (I'll add a check to avoid this)  
default folders used for lookups can be modified in Settings.py  


## Dependencies  
MusiStrata  
Fluidsynth  
SOX

## Future  
Currently supports rendering from samples and soundfonts. It works quite nicely, and the intermediation with instruments settings can allow for customization later on.  

I'm wondering how to handle missing files or files with no audio, maybe resample with adjusted frequency from neighbouring files?  
Also could create compound instruments? This could be easily done with another custom Loader built on the previous two loaders (and could even recursively calll this new loader).  

I would also greatly appreciate a built-in humanization feature when loading the samples (slight noise added, slight filtering?)  

I need to set the line between what this library needs to handle and what is the responsibility of the user, or other libraries (MusiStrata, and a MusiStrata Generator).  

To be added
- Add support for non-wav samples  
- Differentiating between mono and stereo samples    
- Handling SoundFonts                                                                           -> DONE
- Create an actual dispatcher based on an instrument knowledge base                             -> ONGOING
- Add sound effects/mastering such as reverb and filters  
- Handle samples which are too small compared to requested length
- Take decay enveloppe into account to pad song
- Add decay duration as a field of instrument settings                                          -> DONE  
- Enable looping generation?
- Add cache clearing for generated soundfont samples
- Adjust song end timing depending on instruments decay timing (long decay means OOB values)
- Perform instruments names collision check  
- Implement limits to number of samples loaded concurrently  


Other stuff, I'll see how it goes.

I'd like to create a python synth as well, to be plugged in as well. We'll see how it goes.  
