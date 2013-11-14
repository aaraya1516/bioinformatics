# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:05:10 2013

@author: alejandro.araya
"""

#Protein Translation Problem: Translate an RNA string into an amino acid string.
#     Input: An RNA string Pattern.
#     Output: The translation of Pattern into an amino acid string Peptide.
#
#CODE CHALLENGE: Solve the Protein Translation Problem.
#
#Notes:
#
#The “Stop” codon should not be translated, as shown in the sample below.
#For your convenience, we provide a downloadable RNA codon table indicating which codons encode which amino acids.

#Sample Input:
#     AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

#Sample Output:
#     MAMAPRTEINSTRING
     

from os import path, access, R_OK  # W_OK for write permission.
#import time
#import regex

PATH='../approx.txt'
if path.isfile(PATH) and access(PATH, R_OK):
    print "Genome File Found!";
    d = {}
    with open(PATH) as f:
        for line in f:
            (key, val) = line.split()
            d[int(key)] = val