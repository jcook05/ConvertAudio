import os
import os.path
import sys
import re
import subprocess
from optparse import OptionParser

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

files = []

# r=root, d=directories, f = files
for r, d, f in os.walk(d):
    for file in f:
        if '.m4a' in file:
            files.append(os.path.join(r, file))
        if '.mp3' in file:
            files.append(os.path.join(r, file))
filelist = open("filelist", "w")
for f in files:
    print(f)
    filelist.write(f + "\n")
    