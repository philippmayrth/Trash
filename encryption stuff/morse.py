#! /usr/bin/env python
#
# Name: caesar.py
#
# Created by Philipp Mayr on 2. Oct, 2013 Germany
# License: CC - BY (Germany)
#
# 

class morse():
    asciiTable = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',  't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '?', ]
    morseTable = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','.----','..---','...--','....-','.....','-....','--...','---..','----.','-----','--..-','.-.-.-','..--..']

    encodeTable = dict(zip(asciiTable, morseTable)) # {'a' = '.-'}
    decodeTable = dict(zip(morseTable, asciiTable)) # {'.-' = 'a'}


    def encode(plainText):
        encodedText = ""
        plainText = plainText.lower()
        for i in plainText:
            encodedText = encodedText + self.encodedTable[i] + " "

        return encodedText

    def decode(encodedText):
        plainText = ""
        for i in encodedText:
            palinText = plainText + self.decodeTable[i] + " "
        
        return plainText

    def defcode(encodedText):
        return self.decode(encodedText)


if __name__ == "__main__":
    print "lab"
    m = morse()
    while 1:
        print "1. Encode"
        print "2. Decode"
        option = raw_input("Select: ")
    
