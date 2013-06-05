#! /usr/bin/env python3
#
# Name: caesar.py
#
# Created by Philipp Mayr on 5. July, 2013 Germany
# License: CC - BY (Germany)
#
# 

Alphabet = "abcdefghijklmnopqrstuvwxyz"
        
def encrypt(message, key):
    message = message.lower()
    key = key.lower()
    i = Alphabet.index(key[0])
    chipper = Alphabet[i:] + Alphabet[:i]
    EncMessage = {}
    for i in range(len(message)):
        if message[i] in Alphabet:
            position = Alphabet.index(message[i])
            EncMessage[i] = chipper[position]
        else:
            EncMessage[i] = message[i]
    Result = ""
    for i in range(len(EncMessage)):
        Result = Result + EncMessage[i]
    return Result


def decrypt(message, key):
    message = message.lower()
    key = key.lower()
    i = Alphabet.index(key[0])
    chipper = Alphabet[i:] + Alphabet[:i]
    DecMessage = {}
    for i in range(len(message)):
        if message[i] in Alphabet:
            position = chipper.index(message[i])
            DecMessage[i] = Alphabet[position]
        else:
            DecMessage[i] = message[i]
    Result = ""
    for i in range(len(DecMessage)):
        Result = Result + DecMessage[i]
    return Result


def guess(message, language="en"):
    # check if the text makes any of sense at all
    # by comparing the moast common english words with all words in the encrypted message
    wordlist = ["the", "be", "to", "off", "and", "in", "that", "have", "it", "for", "he", "this", "is"]
    positives = {}
    for i in range(len(Alphabet)):
        key = Alphabet[i]
        decrypted = decrypt(message, key)

        words = decrypted.split(" ")
        hits = 0
        for x in range(len(words)):
            if words[x] in wordlist:
                hits = hits +1
                positives[key] = str(hits)
            

        #print ("Key: "+key+" message: "+decrypted)
        #print (positives)
    try:
        # spit out the moast certain letter
        GuessedKey = max(positives)
        return GuessedKey
    except:
        return 1


if __name__ == "__main__":
    
    import sys

    try:
        ShellArgComand = sys.argv[1].lower()
    except:
        ShellArgComand = "--help" # display helt if there is no arg given
    
    if ShellArgComand == "-h" or ShellArgComand == "--help":
        print ("You have the following options:")
        print ("")
        print (" -e, --encrypt  <key> <file>")
        print (" -d, --decrypt  <key> <file>")
        print (" -g, --guess --Print  <file>")
        print (" -g, --guess --gKey   <file>")
        print ("")
        print ("./caesar.py -g -p infile > outfile")
        print ("")
        sys.exit()


    EncKey = sys.argv[2]
    FPath = sys.argv[3]
    
    try:
        MFile = open(FPath)
        Message = MFile.read()
    except:
        print ("Could not open file.", file=sys.stderr)
        print ("") 
        sys.exit(1)
        

    if ShellArgComand == "-e" or ShellArgComand == "--encrypt":

        EncMessage = encrypt(Message, EncKey)
        
        print (EncMessage)
        sys.exit(0)


    elif ShellArgComand == "-d" or ShellArgComand == "--decrypt":

        DecMessage = decrypt(Message, EncKey)

        print (DecMessage)
        sys.exit(0)
        
    elif ShellArgComand == "-g" or ShellArgComand == "--guess":

        GuessedKey = guess(Message)
        if GuessedKey == 1:
            print ("There was an error", file=sys.stderr)

        Mode = sys.argv[2].lower()
        if Mode == "-p" or Mode== "--print":
            GuessedMessage = decrypt(Message, GuessedKey)
            print (GuessedMessage)
        elif Mode == "-k" or Mode == "--gkey":
            print ("The key guessed is: ", GuessedKey)
