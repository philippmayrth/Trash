#! /usr/bin/env python
#
# Name: caesar.py
#
# Created by Philipp Mayr on 25. Nov, 2013 Germany
# License: CC - NC - BY (Germany)
#
#

import sys

python3 = ['print', 'continue', 'return', 'from', 'elif', 'if', 'else', 'while', ' for ', 'try', 'except', 'class', ' and ', ' or ', ' not ', ' in ', 'range', 'break', 'True', 'True', 'False', 'False', 'None', 'open', 'read', 'write']
teuton =  ['drucke', 'weiter', 'zurueck', 'von', 'wennsonst', 'wenn', 'sonst', 'solange', ' fuer ', 'versuche', 'ausser', 'klasse', ' und ', ' oder ', ' nicht ', ' im ', 'bereich', 'abbrechen', 'wahr', 'ja', 'falsch', 'nein', 'nix', 'oeffnen', 'lesen', 'schreiben']



if __name__ == "__main__":
    
    mode = ""
    sourceFile = ""
    destFile = ""
    
    if len(sys.argv) > 3:
        mode = sys.argv[1]
        sourceFile = sys.argv[2]
        destFile = sys.argv[3]
    else:
        print "teuton teu2py source.teu dest.py"
        print "teuton py2teu source.py dest.teu"
        exit()
    

    if mode == "teu2py":
        teu2py = dict(zip(teuton, python3))
        fTeu = open(sourceFile, "r")
        assamble = ""
    
        for line in fTeu.readlines():
            for teu in teuton:
                if teu in line:
                    line = line.replace(teu, teu2py[teu])
            assamble = assamble + line
            
        fTeu.close()

        fPy = open(destFile, "w")
        fPy.write(assamble)
        fPy.close()

    elif mode == "py2teu":
        py2teu = dict(zip(python3, teuton))
        fPy = open(sourceFile)
        assamble = ""

        for line in fPy.readlines():
            for py in python3:
                line = line.replace(py, py2teu[py])
            assamble = assamble + line

        fPy.close()

        fTeu = open(destFile, "w")
        fTeu.write(assamble)
        fTeu.close()
