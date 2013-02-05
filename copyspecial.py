#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
# file is special if there's 2 _ , find special files and list abspath
# --todir copy all the special files to the dir
# --tozip zip all the special files, zip -j

def findSpecial(sentDir):
  specialList = []
  files = os.listdir(sentDir)
  for eachFile in files:
    if re.search(r'__.*?__', eachFile):
      specialList.append(eachFile)
  return specialList

def printSpecial(argList):
  for sentDir in argList:
    files = findSpecial(sentDir)
    for eachFile in files:
      print os.path.abspath(os.path.join(sentDir, eachFile))

def copyToDir(argList):
  targetDir = argList[0]
  if not os.path.exists(targetDir):
    os.mkdir(targetDir)
  for sourceDir in argList[1:]:
    files = findSpecial(sourceDir)
    for eachFile in files:
      homeDir = os.path.abspath(os.path.join(sourceDir, eachFile))
      shutil.copy(homeDir, targetDir)


def copyToZip(argList):
  zipFiles = ''
  targetZip = argList[0]
  for sourceDir in argList[1:]:
    files = findSpecial(sourceDir)
    for eachFile in files:
      zipFiles  += ' ' + eachFile
  zipCommand = 'zip -j ' + targetZip + zipFiles
  print 'About to run: ' + zipCommand

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:1]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:1]

  if todir:
    copyToDir(args)
  elif tozip:
    copyToZip(args)
  else: 
    printSpecial(args)
  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
