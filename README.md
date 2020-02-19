# ConvertAudio
Convert .m4a and .mp3 to .aac

# Summary
 Project to convert music from an Ipod or Itunes directory to .aac format usable by any music player.   This project leverages python and ffmpeg to convert .m4a and .mp3 
 music from a target directory to .aac.   The end result will be converted .aac audio, to include metadata, located in your target music directory by Album and Artist. 
 Unfortunately Ipods are going the way of the dinosaur.   I loved my Ipod classic and am not too keen on the newer models.   That being said, I wrote this code so that I could quickly extract and convert my music from my old Ipod and be ready to load it onto a new device.   

## Usage

python3 ConvertAudio.py -t <target/music/dir/path> -m <desired/metadata/path> -i <converted/music/path>


## Setup

  Install ffmpeg for Linux (Ubuntu).   ffmpeg should be available in the Unviverse repository.   Install via apt.

   sudo add-apt-repository universe
   sudo apt update
   sudo apt install ffmpeg
 
 You could also add as an ansible task:  

 - name: Install ffmpeg
   apt: 
     name: ['ffmpeg']
     state: latest


## Notes

  I'm sure there are some areas of this code that could be more elegant.   I'm open to suggestions, but this code worked well for me. 

