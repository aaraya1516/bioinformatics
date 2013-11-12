# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:28:23 2013

@author: alejandro.araya
"""

#Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
#     Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
#     Output: All most frequent k-mers with up to d mismatches in Text.
#
#CODE CHALLENGE: Solve the Frequent Words with Mismatches Problem.
#
#Sample Input:
#     ACGTTGCATGTCGCATGATGCATGAGAGCT 4 1
#Sample Output:
#     GATG ATGC ATGT

import re

# Gene we're seq.
gnome = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
gnomeLen = len(gnome);

# K-mer length
k=4;

# Variations/Mismatches
d=1;

nucleotides = ['A','T','C','G']

codons = [];
variantCodons = []

print "Starting Loop"
i = 0
while (i <= gnomeLen-k):
    # count 1 plus k-mer length
    endRange = i+k;
    #value of string 
    strRange = gnome[i:endRange];
    codons.append(strRange);
    #m = regex.findall("("+strRange+")", gnome, overlapped=True)
    i += 1;
    
print "Found codons in genome: "+str(codons);

for codon in codons:
    j = 0;
    variantCodons.append(codons)
    while j<=k:
        codonAsList = list(codon);
        codonAsList[j] = '.'
        print "codonAsList:"+str(j)+" "+str(codonAsList)
        variantCodons.append("".join(codonAsList))
        j +=1;
for varCodon in variantCodons:
    m = re.search(varCodon,gnome)
    print m