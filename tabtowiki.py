# -*- coding: utf-8 -*-
# tab to mediawiki
import re
import sys
import os
import string
import argparse

# Define the command line arguments
parser = argparse.ArgumentParser(description="Convert tab to mediawiki")
parser.add_argument('--filename', help='Filename to read from', default=None)
args = parser.parse_args()

# Decide whether to read from file or standard input
if args.filename:
    path = "./"
    filename = args.filename
    fileandpath = os.path.join(os.path.expanduser(path), filename)
    fileobj = open(fileandpath, 'r') # open for reading
    lines = fileobj.readlines() # read all lines into array
    fileobj.close()
else:
    lines = sys.stdin.readlines()

# clean nobreaking space
printable = set(string.printable)
out = []
for l in lines:
    a = l.replace(u"\xc2", "").replace(u"\xa0", " ")
    out.append(a)
lines = out

# Patterns
ptrn = '[\w \:;,\."\(\)\-\+\?\–\’\']'
p0 = r'<' # allows < as substitute for * bullet points
p1 = r'^(' + ptrn + '+)$' # first level heading - part or chapter
p2 = r'^\t(' + ptrn + '+)$' # second level heading - chapter or section
p3 = r'^\t\t(' + ptrn + '+)$' # third level section or subsection
p31 = r'^\t\t\t(' + ptrn + '+)$'
p4 = r'\t' # allows bullet points at same tab level in source file
p5 = r'§(.+)$' # allows tabbed sections of text from reports etc

leveldict = {p0:'*', p1:"===\\1===", p2:"====\\1====", p3:"=====\\1=====", p31:"\n'''\\1'''"}

lst = lines
for key in leveldict.keys():
    lst = list(map(lambda x: re.sub(key, leveldict[key], x), lst))
lst = list(map(lambda x: re.sub(p4, '', x), lst))
lst = list(map(lambda x: re.sub(p5, '\\1\n', x), lst))
print(''.join(lst))
