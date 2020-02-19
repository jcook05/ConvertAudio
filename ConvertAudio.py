import os
import os.path
import sys
import random
from optparse import OptionParser


title = ""
artist = ""
album = ""

"""Write audio file metadata to a file"""
def getMetaData(filepath, metafilepath):
  command = "ffmpeg -i " + filepath + " -f ffmetadata " + metafilepath + " -y"
  os.system(command)

"""Set title, artist and album attributes"""
def setAttributes(metapath):
   global title
   global artist
   global album

   title = ""
   artist = ""
   album = ""
   print(metapath)
   f = open(metapath, 'rb')
   lines = f.readlines()
   for line in lines:
    strline = str(line)
    strline = s = strline.rstrip(os.linesep)
  
    if "title" in strline:
      title = strline.split("=")[1][:-3]
      print(title)
    if "artist" in strline:
      artist = strline.split("=")[1][:-3]
      print(artist)
    if "album" in strline:
      album = strline.split("=")[1][:-3]
      print(album)


#Main
if __name__=="__main__":   

#Define Options
    parser = OptionParser()
    parser.add_option('-t','--targetdir',help='targetdirectory',default=None)
    parser.add_option('-m', '--metadir', help='meta data directory',default=None)
    parser.add_option('-i', '--musicdir', help='music directory',default=None)
      
    #Add output file   	
    (args,args_extra) = parser.parse_args()
	
#Define exceptions
    if (args.targetdir is None):
       parser.error("no targetdir specified")


d = args.targetdir
m = args.metadir
i = args.musicdir

files = []
filenames = []


# Get a list of .m4a and .mp3 files from target dir.  Target dir should be where your
# Ipod or Itunes music is stored. 
for r, d, f in os.walk(d):
    for file in f:
        if '.m4a' in file:
            files.append(os.path.join(r, file))
        if '.mp3' in file:
            files.append(os.path.join(r, file))

for f in files:
   
    last = f.split('/')[-1][:-4]
    
    if last in filenames:
       last = last + str(random.randint(1,100))
    
    filenames.append(last)

    filepath = m + "/" + last
    metapath = m + "/" + last + ".txt"
    
    if os.path.isfile(metapath):
      setAttributes(metapath)
    else:
      getMetaData(f, metapath)
      setAttributes(metapath)

    artistdir = i + "/" + artist.replace(".", "")
    print(artistdir)
    albumdir = artistdir + "/" + album.replace(".", "")
    print(albumdir)
    if not (os.path.isdir(artistdir)):
      command = "mkdir " + "\"" + artistdir + "\""
      print(command)
      os.system(command)
    if not (os.path.isdir(albumdir)):
      command = "mkdir " + "\"" + albumdir + "\""
      print(albumdir)
      print(command)
      os.system(command)
    
    command = "ffmpeg -y -i " + f +  " -acodec copy " + "\"" + albumdir + "/" + title.replace(" ", "") + ".aac"+ "\""
    print(command)
    os.system(command)