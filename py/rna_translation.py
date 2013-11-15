# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14

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
     

from os import path  # W_OK for write permission.
#import time
#import regex

PATH="../RNA_codon_table_1.txt"
if path.isfile(PATH):
    print "RNA Dictionary File Found!";
    d = {}
    with open(PATH) as f:
        for line in f:
            #print len(line)
            if len(line) == 6:
                (key, val) = line.split()
                d[key] = val
                #print d[key]
            else:
                d[line] = ""
else:
    print "RNA Dictionary File NOT Found! "
    print "Path is:"+PATH

# SHould we use the example?
useExample = 1;

# RNA to translate
rnaPath="../rnaInput.txt"
if path.isfile(rnaPath) and useExample==1:
    print "RNA String Found!"
    rnaFile = open(rnaPath ,"r");
    rnastr = rnaFile.read();
    rnaFile.close();
else:
    rnastr = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA";
    
rnastrLen = len(rnastr);

# Codon size we're translating
k = 3;

#counter starting at 0
i = 0;

# output string
outPutString = "";

# Loop through RNA strand until we reach the end
while (i <= rnastrLen-k):
    #print i

    # index val for the end of the frame we're looking at
    endRange = i+k;
    #print endRange
    #value of codon we're looking at
    ksizeCodon = rnastr[i:endRange];
    #print ksizeCodon;
    
    # get the protein from the dictionary
    protein = d.get(ksizeCodon)
    
    if str(protein) != "None":
        #print protein
        outPutString = outPutString+str(protein)
        
    if 68<len(outPutString)<80:
        print protein
        print ksizeCodon
    i += 3;

#Example protein Output for comparision for accuracy
rnaOutputComp="../rnaOutputComp.txt"
if path.isfile(rnaOutputComp) and useExample==1:
    print "Protien String Found!"
    proteinFile = open(rnaOutputComp ,"r");
    proteinstr = proteinFile.read();
    proteinFile.close();

if outPutString == proteinstr:
    print "Successful Match!"
else:
    print "Protein Seq Not Matching: "+outPutString
    print "Size diff (output - comparable): "+str(len(outPutString)-len(proteinstr))