"""
Copyright 2014 Ethan Porter
This module includes both a constructor for a textParse object and static methods.
Use the constructor for a specific, repeated use of this class.
Otherwise, you can use the static methods to parse your text.
"""

class textParse:

# require: splitchars is a list of single character strings
    def __init__(self,splitchars):
        self.SC = splitchars

# require: splitchar is a single character string
# ensure: splitchar is added to list of splitchars
    def nextSC(self,splitchar):
        self.SC.append(splitchar)

# ensure: list of splitchars is empty
    def clearSC(self):
        self.SC = []

    def parseFile(self,pathway,option):
        a = self.readFile(pathway,option)
        for i in self.SC:
            a = textParse.parse(a,i)
        return a

    def parseString(self,string):
        a = string
        for i in self.SC:
            a = textParse.parse(a,i)
        return a

# require: pathway is string containing the file's pathway
#            option is an open option, e.g. 'r'
# ensure: return contents of file as string
    @staticmethod
    def readFile(pathway,option):
        f = open(pathway,option)
        instring = f.read()
        f.close()
        return instring

# require: input is a string, splitChar is the character to split by
# ensure: return split up list of strings
    @staticmethod
    def parse(inpt,splitChar):
        if type(inpt) is str:
            newArray = inpt.split(splitChar)
            return newArray
        elif isinstance(inpt,list):
            newArray = []
            for i in inpt:
                newArray.append(textParse.parse(i,splitChar))
            return newArray

# require: input is a string, file is name of the file to write to or create
# ensure: file now contains input
    @staticmethod
    def write(inpt,fileName):
        f=open(fileName,'w')
        f.write(str(inpt))
        f.close()