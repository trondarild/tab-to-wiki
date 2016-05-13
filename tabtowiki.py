# -*- coding: utf-8 -*-
# tab to mediawiki
import re
import sys
import os

# print "got " + str(sys.argv)


path = "./"
filename = "tablist.txt"
# expand and join path and filename
fileandpath = os.path.join(os.path.expanduser(path), filename)
fileobj = open(fileandpath, 'r') # open for reading
lines = fileobj.readlines() # read all lines into array
fileobj.close()

ptrn = '[\w :;,\."\(\)\-\+\?\–\’\']'
p0 = r'<' # allows < as substitute for * bullet points
p1 = r'^(' +ptrn+ '+)$'
p2 = r'^\t(' +ptrn+ '+)$'
p3 = r'^\t\t(' +ptrn+ '+)$'
p4 = r'\t' # allows bullet points at same tab level in source file
p5 = r'§(.+)$' # allows tabbed sections of text from reports etc

dict = {p0:'*', p1:"===\\1===", p2:"====\\1====", p3:"\n'''\\1'''"}#, p4:''}


lst = lines
for key in dict.keys():
  lst = map(lambda x: re.sub(key, dict[key], x), lst)
lst = map(lambda x: re.sub(p4, '', x), lst)
lst = map(lambda x: re.sub(p5, '\\1\n', x), lst)
print ''.join(lst)

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
