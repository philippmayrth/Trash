#! /usr/bin/env python
#
# Name: caesar.py
#
# Created by Philipp Mayr on 26. Nov, 2013 Germany
# License: CC - NC - BY (Germany)
#
#

import os

def sag(text):
    cmd = "say " + text
    os.system(cmd)