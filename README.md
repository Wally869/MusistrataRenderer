# Musistrata Renderer  

Creating an interface to render Musistrata-defined songs using a variety of sources (soundfonts, user-defined samples, custom synthesizer...)  


## Why?  

DAWs do not allow for direct scripting/control over their engines and their file formats are proprietary and undocumented. VSTs Hosts are a mess (compatibility issues between 2.0 and 3.0), and usually encrypt their data. SF2 are low quality, or need heavy mastering as well as a variety of tools for rendering (FluidSynth & Sox) with some issues (the Fluidsynth version distributed on VCPKG is not the latest build and suffers a type error which prevents the use of soundfonts bigger than ~2gb).

Since I wanted a fully automated pipeline to create songs and considering how fractured the musical production environment seems to be, I thought it easier to try to create a simple interface which would hide all the complexity. 

## Current  

SamplesLoader.py implements a basic samples loader: give an instrument name and a target note as input for __call__, and it will check whether the sample has already been loaded or not.  
If the sample has not been loaded, it will load it fully and save it in memory as an np.ndarray. Sample files must be in the path "Samples/Instrument-Name/Instrument-Name_Height.wav" (so Piano C0 would be in Samples/Piano/Piano_0.wav).  

AudioUtils.py contains some functions to add panning and delay to audio input. Careful: We use constant power pan, so I believe a panning of 0.5 (so panned to the center) will result in a slight decrease in volume (lower sound amplitude). Will check it out.    

Dispatcher.py contains the functions responsible to render the MusiStrata.Track and MusiStrata.Song objects.

## To Note    
Dispatcher.py directly implements a decay enveloppe to the sound, to avoid 

## Future  
It's a very early WIP, and a huge mess. It works to render from samples (see Media/sampleRendered.mp3 to see an example of a rendered file with added delay), but the structure will be rewritten. I'm uploading now for future reference and to share the simple scripts I've already got.  

To be added
- Add support for non-wav samples  
- Differentiating between mono and stereo samples    
- Handling SoundFonts    
- Create an actual dispatcher based on an instrument knowledge base   
- Add sound effects/mastering such as reverb  

Other stuff, I'll see how it goes.

I'd like to create a python synth as well, to be plugged in as well. We'll see how it goes.  
