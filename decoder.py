#!/usr/bin/env python
import sys

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

def decode_element(e):
        if e == "":
                return ""
        try:
                return element[e]
        except:
                print "Unexpected element: " + e
                sys.exit()
def decode_string(s):
        decodedstring = ""
        for word in s:
		print word
                e = ""
                for char in word:
                        if(char == "."):
                                decodedstring = decodedstring + decode_element(e) + "."
                                e = ""
                        elif(char == ","):
                                decodedstring = decodedstring + decode_element(e) + ","
                                e = ""
                        elif(char.islower() and len(e) == 1):
                                e += char
                                decodedstring = decodedstring + decode_element(e)
                                e = ""
                        elif(char.isupper() and len(e) == 1):
                                decodedstring = decodedstring + decode_element(e)
                                e = char
                        else:
                                decodedstring = decodedstring + decode_element(e)
                                e = char
                decodedstring = decodedstring + " "
        return decodedstring

if __name__ == "__main__":
        print decode_string(sys.argv[1:])

