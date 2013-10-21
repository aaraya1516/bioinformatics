#
# Pattern Matching
#
#


from os import path, access, R_OK  # W_OK for write permission.
import time

PATH='../genome.txt'
useFile = 1;
if path.isfile(PATH) and access(PATH, R_OK) and useFile == 1:
    print "Genome File Found!"
    useGenomeFile = raw_input('To use file press 1:')
    #open the file
    if useGenomeFile == '1':
        genomeFile = open(PATH ,"r")
        genomeStr = genomeFile.read();
        genomeFile.close();
    else:
        PATH = raw_input('What is the path to the genome?')
        genomeFile = open(PATH ,"r")
        genomeStr = genomeFile.read();
        genomeFile.close();
    #print "String:", genomeStr
else:
    genomeStr = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
	
pattern = raw_input('What pattern are you looking for?')

patternIndex = ""
lastLoc = locationNow = i = 0
genomeLength = len(genomeStr)
lastiMark = genomeLength - len(pattern)

while (i < lastiMark)