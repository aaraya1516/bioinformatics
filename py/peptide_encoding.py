# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 19:18:52 2013

@author: alejandro
"""

#We say that a DNA string Pattern encodes an amino acid string Peptide if the
# RNA string transcribed from either Pattern or its reverse complement Pattern 
# translates into Peptide.
#
#Peptide Encoding Problem: Find substrings of a genome encoding a given amino 
# acid sequence.
#     Input: A DNA string Text and an amino acid string Peptide.
#     Output: All substrings of Text encoding Peptide (if any such substrings exist).
#
#CODE CHALLENGE: Solve the Peptide Encoding Problem.
#
#Sample Input:
#     ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
#     MA
#
#Sample Output:
#     ATGGCC
#     GGCCAT
#     ATGGCC
#
#Note: The solution may contain repeated strings if the same string occurs more
# than once as a substring of Text and encodes Peptide.

from os import path  # W_OK for write permission.

PATH="../RNA_codon_table_1.txt"
if path.isfile(PATH):
    print "RNA Dictionary File Found!";
    d = {}
    with open(PATH) as f:
        for line in f:
            #print len(line)
            if len(line) == 6:
                (val, key) = line.split()
                d[key] = val
                #print d[key]
            else:
                d[line] = ""
else:
    print "RNA Dictionary File NOT Found! "
    print "Path is:"+PATH

useExample = 2;

# RNA to translate
rnaPath="../rnaInput.txt"
if path.isfile(rnaPath) and useExample==1:
    print "RNA String Found!"
    rnaFile = open(rnaPath ,"r");
    rnastr = rnaFile.read();
    rnaFile.close();
else:
    rnastr = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA";
    
rnastrLen = len(rnastr);

# Encoded peptide
encPeptide = "MA";

# codon (k-mer) size we're looking at:
k=3;

# List of RNA codons that encoded the translated peptide
rnaCod = [];

for letter in encPeptide:
    rnaCod.append(d.get(letter));

i=0;
while i < rnastrLen-len(encPeptide):
# index val for the end of the frame we're looking at
    endRange = i+k;
    #print endRange
    #value of codon we're looking at
    ksizeCodon = rnastr[i:endRange];
    #print ksizeCodon;

print rnaCod;