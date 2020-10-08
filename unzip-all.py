#!/usr/bin/python
import os, zipfile

#unzips all the zip folders down 1 level from the root.

for filename in os.listdir("."):
     if filename.endswith(".zip"):
        print (filename)
        name = os.path.splitext(os.path.basename(filename))[0]
        if not os.path.isdir(name):
            try:
                zip = zipfile.ZipFile(filename)
                os.mkdir(name)
                zip.extractall(path=name)
            except zipfile.BadZipfile:
                print ("BAD ZIP: "+filename)
                try:
                    os.remove(filename)
                except OSError as e: # this would be "except OSError, e:" before Python 2.6
                    if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
                        raise # re-raise exception if a different error occured       
     