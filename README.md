# Musistrata Renderer  

Creating an interface to render Musistrata-defined songs using a variety of sources (soundfonts, user-defined samples, custom synthesizer...)  


## Why?  

DAWs do not allow for direct scripting/control over their engines and their file formats are proprietary and undocumented. VSTs Hosts are a mess (compatibility issues between 2.0 and 3.0), and usually encrypt their data. SF2 are low quality, or need heavy mastering as well as a variety of tools for rendering (FluidSynth & Sox) with some issues (the Fluidsynth version distributed on VCPKG is not the latest build and suffers a type error which prevents the use of soundfonts bigger than ~2gb).  
UPDATE: FluidSynth now distributes v2.2 binaries for Windows directly from github since 3 weeks ago, so this is not an issue anymore (https://github.com/FluidSynth/fluidsynth/releases/tag/v2.2.0)   


Since I wanted a fully automated pipeline to create songs and considering how fractured the musical production environment seems to be, I thought it easier to try to create a simple interface which would hide all the complexity. 

## Current  

Can load samples from a Samples folder (handled in samples loader file), or from a soundfont. Soundfont imports need to create an intermediary midi file, then create a wav file which is then read. Current setup uses MusiStrata to create a midi file, which is then rendered to RAW by fluidsynth and then to wav by SOX. Bit convoluted but I had issues with rendering midi to wav with fluidsynth on windows for some reason. Plus the conversion process would make FluidSynth play the sounds and would block execution while doing it, so using the raw format allowed to avoid this problem. Not sure if can fix, will check it out.  


AudioUtils.py contains some functions to add panning and delay to audio input. Careful: We use constant power pan, so I believe a panning of 0.5 (so panned to the center) will result in a slight decrease in volume (lower sound amplitude). Will check it out.    

Renderer.py contains the functions responsible to render the MusiStrata.Track and MusiStrata.Song objects


## Future  
It's a very early WIP, and a huge mess. It works to render from samples (see Media/sampleRendered.mp3 to see an example of a rendered file with added delay), but the structure will be rewritten. I'm uploading now for future reference and to share the simple scripts I've already got.  

To be added
- Add support for non-wav samples  
- Differentiating between mono and stereo samples    
- Handling SoundFonts  -> DONE
- Create an actual dispatcher based on an instrument knowledge base   -> ONGOING
- Add sound effects/mastering such as reverb and filters  
- Handle samples which are too small compared to requested length
- Take decay enveloppe into account to pad song
- Add decay duration as a field of instrument settings
- Enable looping generation?
- Add cache clearing for generated soundfont samples
- Adjust song end timing depending on instruments decay timing (long decay means OOB values)

Other stuff, I'll see how it goes.

I'd like to create a python synth as well, to be plugged in as well. We'll see how it goes.  
