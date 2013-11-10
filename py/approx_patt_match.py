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
#import time
import regex

PATH='../approx.txt'
useFile = 1;
if path.isfile(PATH) and access(PATH, R_OK) and useFile == 1:
    print "Genome File Found!";
    #useGenomeFile = raw_input('To use file press 1:');
    #open the file
    if '1' == '1':
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
    genomeStr = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT";

# What are the possible combos of base^t
base= "AGGTACAT";#"ATTCTGGA"
output="";
indG="";
dblsMatch=[];
indList=[];
m=regex.findall("(AGGTACAT){s<=5}", genomeStr, overlapped=True)
#m=regex.findall()
#print m
for mm in m:
    indG = genomeStr.index(mm);
    if indG not in indList:
        indList.append(indG);
    else:
        dblsMatch.append(indG);
    #print output;
indList.sort();
for ind in indList:
    output = output+" "+str(ind);
print output;
print "Length m:"+str(len(m))
print "length indList:"+str(len(indList))
print "Length Doubles:"+str(len(dblsMatch))
print "m minus dbls Size:"+str(len(m)-len(dblsMatch))
print "Difference:"+str(len(indList)-(len(m)-len(dblsMatch)))
#print "Clalculated:"+str(len(base)**5)