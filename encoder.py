#!/usr/bin/env python
import sys, string

element = {
 "H"  : "A",
 "He" : "B",
 "Li" : "C",
 "Be" : "D",
 "B"  : "E",
 "C"  : "F",
 "N"  : "G",
 "O"  : "H",
 "F"  : "I",
 "Ne" : "J",
 "Na" : "K",
 "Mg" : "L",
 "Al" : "M",
 "Si" : "N",
 "P"  : "O",
 "S"  : "P",
 "Cl" : "Q",
 "Ar" : "R",
 "K"  : "S",
 "Ca" : "T",
 "Sc" : "U",
 "Ti" : "V",
 "V"  : "W",
 "Cr" : "X",
 "Mn" : "Y",
 "Fe" : "Z",
 ","  : ",",
 "."  : "."
}

def encode_char(e):
        for el, char in element.iteritems():
                if char == string.upper(e):
                        return el
        return e

def decode_string(s):
        encodedstring = ""
        for word in s:
                for char in word:
                        encodedstring = encodedstring + encode_char(char)
		encodedstring = encodedstring + " "
        return encodedstring

if __name__ == "__main__":
        print decode_string(sys.argv[1:])

