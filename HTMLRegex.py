#!/usr/bin/python

import sys
import re

def remove_HTML_tags(filename):
	openfile = open(filename, 'r')
	for line in openfile:
		#This matches HTML tags, makes them '', 
		#and creates a list of the remaining text.
		text = re.compile(r'<.*?>').split(line)
		for words in text:
			if words != '':
				print words,

def main():
  if len(sys.argv) != 2:
    print 'usage: ./HTMLregex.py file'
    sys.exit(1)

  filename = sys.argv[1]
  print filename
  remove_HTML_tags(filename)

if __name__ == '__main__':
  main()