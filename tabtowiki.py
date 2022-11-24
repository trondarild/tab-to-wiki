# -*- coding: utf-8 -*-
# tab to mediawiki
import re
import sys
import os
import string

# print "got " + str(sys.argv)


path = "./"
filename = "tablist.txt"
# expand and join path and filename
fileandpath = os.path.join(os.path.expanduser(path), filename)
fileobj = open(fileandpath, 'r') # open for reading
lines = fileobj.readlines() # read all lines into array
fileobj.close()

# clean nobreaking space
printable = set(string.printable)
out = []
for l in lines:
  # TODO: change to work with p3x
  a = l.decode("utf-8").replace(u"\xc2", "").replace(u"\xa0", " ").encode("utf-8")
  #a = filter(lambda x: x in printable, a)
  out.append(a)
lines = out
#lines = map(lambda x: re.sub(u'\xc2', u'', x), lines)
#lines = map(lambda x: re.sub(u'\xa0', u' ', x), lines)

# TODO does not appear to work with p3x
ptrn = '[\w \:;,\."\(\)\-\+\?\–\’\']'
p0 = r'<' # allows < as substitute for * bullet points
p1 = r'^(' +ptrn+ '+)$' # first level heading - part or chapter
p2 = r'^\t(' +ptrn+ '+)$' # second level heading - chapter or sectinon
p3 = r'^\t\t(' +ptrn+ '+)$' # third level section or subsection
p31 = r'^\t\t\t(' +ptrn+ '+)$'

p4 = r'\t' # allows bullet points at same tab level in source file
p5 = r'§(.+)$' # allows tabbed sections of text from reports etc

leveldict = {p0:'*', p1:"===\\1===", p2:"====\\1====", p3:"=====\\1=====", p31:"\n'''\\1'''"}#, p4:''}


lst = lines
for key in leveldict.keys():
  lst = map(lambda x: re.sub(key, leveldict[key], x), lst)
lst = map(lambda x: re.sub(p4, '', x), lst)
lst = map(lambda x: re.sub(p5, '\\1\n', x), lst)
print (''.join(lst))

##debug
'''
outlines = []
for l in lines:
  subs = l
  for key, val in leveldict.iteritems():
    subs = re.sub(key, val, subs)
  outlines.append(subs) 
print "".join(outlines)
'''

'''
def repltab(str):
  return p2.sub(r'=\1=', str)

lst = lines
while (any('\t' in string for string in lst)):
  lst =  map(lambda x: repltab(x), lst)
  print lst

print lst

# print map(lambda x: p2.match(x), lines)
firstlevel = "==="
repl1 = firstlevel + "\\1" + firstlevel
secondlevel = firstlevel + "="
repl2 = secondlevel + "\1" + secondlevel

lines = map(lambda x: p1.sub(r'===\1===', x), lines)
print lines
lines = map(lambda x: p2.sub(r'====\1====', x), lines)
print lines

print ''.join(lines)

for line in lines:
  print line

print lines

for line in lines:
  res = p2.sub(r'====\1====', line)
  print res
'''
