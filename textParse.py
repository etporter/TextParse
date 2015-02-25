"""
Copyright 2014 Ethan Porter
This module includes both a constructor for a textParse object and static methods.
Use the constructor for a specific, repeated use of this class.
Otherwise, you can use the static methods to parse your text.
"""

class TextParse:

# require: splitchars is a list of single character strings
    def __init__(self,splitchars):
        self.SC = splitchars

# require: splitchar is a single character string
# ensure: splitchar is added to list of splitchars
    def NextSC(self,splitchar):
        self.SC.append(splitchar)

# ensure: list of splitchars is empty
    def ClearSC(self):
        self.SC = []

    def ParseFile(self,pathway,option):
        a = self.readFile(pathway,option)
        for i in self.SC:
            a = textParse.parse(a,i)
        return a

    def ParseString(self,string):
        a = string
        for i in self.SC:
            a = textParse.parse(a,i)
        return a

# require: pathway is string containing the file's pathway
#            option is an open option, e.g. 'r'
# ensure: return contents of file as string
    @staticmethod
    def ReadFile(pathway,option):
        f = open(pathway,option)
        instring = f.read()
        f.close()
        return instring

# require: input is a string, splitChar is the character to split by
# ensure: return split up list of strings
    @staticmethod
    def Parse(inpt,splitChar):
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
    def Write(inpt,fileName):
        f=open(fileName,'w')
        f.write(str(inpt))
        f.close()

    @staticmethod
    def RemoveChar(inpt,char):
        if type(inpt) is str:
            a=inpt.split(char)
            c = ''
            for i in a:
                c += i
            return c

        elif isinstance(inpt,list):
            newList = []
            for i in inpt:
                a=i.split(char)
                c = ''
                for j in a:
                    c+=j
                newList.append(c)
            return newList