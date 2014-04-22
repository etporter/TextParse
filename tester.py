from textParse import *
spltC = ['/']

tParse = textParse(spltC)

string = 'this/is/a/test'

print tParse.parseString(string)