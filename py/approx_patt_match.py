#Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
#     Input: Two strings Pattern and Text along with an integer d.
#     Output: All positions where Pattern appears in Text with at most d mismatches.
#
#CODE CHALLENGE: Solve the Approximate Pattern Matching Problem
#
#Sample Input:
#     ATTCTGGA
#     CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
#     3


from os import path, access, R_OK  # W_OK for write permission.
import time

PATH='../approxgenome.txt'
useFile = 1;
if path.isfile(PATH) and access(PATH, R_OK) and useFile == 1:
    print "Genome File Found!";
    useGenomeFile = raw_input('To use file press 1:');
    #open the file
    if useGenomeFile == '1':
        genomeFile = open(PATH ,"r");
        genomeStr = genomeFile.read();
        genomeFile.close();
    else:
        PATH = raw_input('What is the path to the genome?');
        genomeFile = open(PATH ,"r");
        genomeStr = genomeFile.read();
        genomeFile.close();
    #print "String:", genomeStr
else:
    genomeStr = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA";

# Length of Genome
gnmLength = len(genomeStr);

#How many permutations allowed
t = 3;

# What codons are we trying to match the pattern to?
base = "ATTCTGGA";
baseLength = len(base);

# What are the possible combos of base^t