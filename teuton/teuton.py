#! /usr/bin/env python
#
# Name: caesar.py
#
# Created by Philipp Mayr on 25. Nov, 2013 Germany
# License: CC - NC - BY (Germany)
#
#

import sys
import os

class grammer():
    teu2py = {}
    py2teu = {}
    
    teuton = []
    python3 = []
    
    def read(self):
        python3 = []
        teuton = []
        
        f = open("grammer", "r")
        for i in f.readlines():
            if i[0] != "#" and i[0] != "\n":
                i = i.split("=")
                python3.append(i[0])
                teuton.append(i[1].replace("\n", ""))
        f.close()
        
        self.teuton = teuton
        self.python3 = python3
        
        self.teu2py = dict(zip(teuton, python3))
        self.py2teu = dict(zip(python3, teuton))



syntax = grammer()
syntax.read()
teuton = syntax.teuton
python3 = syntax.python3
teu2py = syntax.teu2py
py2teu = syntax.py2teu

def convertTeu2py(sourceFile, destFile):
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


def convertPy2teu(sourceFile, destFile):
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


if __name__ == "__main__":
    
    mode = ""
    sourceFile = ""
    destFile = ""
    
    if len(sys.argv) > 1 and len(sys.argv) < 3:
        mode = "run"
        sourceFile = sys.argv[1]
    elif len(sys.argv) > 3:
        mode = sys.argv[1]
        sourceFile = sys.argv[2]
        destFile = sys.argv[3]
    else:
        print "teuton teu2py source.teu dest.py"
        print "teuton py2teu source.py dest.teu"
        print "teuton source.teu"
        exit()
    

    if mode == "run":
        destFile = sourceFile + "X" # name.teuX
        convertTeu2py(sourceFile, destFile)
        cmd = "python "+destFile
        os.system(cmd)
    elif mode == "teu2py":
        convertTeu2py(sourceFile, destFile)
    elif mode == "py2teu":
        convertPy2teu(sourceFile, destFile)
