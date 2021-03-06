# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:39:28 2013

@author: alejandro
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

from os import path, access, R_OK  # W_OK for write permission.
import regex, time

PATH='../freq_words_mismatch.txt'
useFile = 1;
if path.isfile(PATH) and access(PATH, R_OK) and useFile == 1:
    print "Genome File Found!";
    useGenomeFile = raw_input('To use file press 1:');
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
    genomeStr = "CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC";

# k-mer length
k = 10;
# Number of mismatches
d = 2;
#
# min number of matches
t=1;
L=len(genomeStr);
output=0;
indG="";
i = 0;
epoch_timeStart = int(time.time())
rangeList = [];
strDict = {};
biggestM = [];

strLength = len(genomeStr)
print "Starting Loop"
while (i <= strLength):
    # count 1 plus k-mer length
    endRange = i+k
    #value of string 
    strRange = genomeStr[i:endRange]
    m = regex.findall("("+strRange+"){s<=2}", genomeStr, overlapped=True)
    #print strRange    
    #print str(m)
    if m != [] and len(strRange) == k:
        strDict[strRange] = len(m)
        rangeList.append(strRange)
        newList = [];
        newStrDict = {};
        
        for codon in m:
            n = regex.findall("("+codon+"){s<=2}", genomeStr, overlapped=True)
            newStrDict[codon] = len(n)
            strDict[strRange] = len(m)+len(n)
            newList.append(strRange)

        if len(m) > len(biggestM):
            biggestM = m;
        #concatString=concatString+" "+strRange
        #print "String: "+strRange
        #print "Count: "+str(genomeStr.count(strRange, i, i+L))        
    i=i+1

print output;
print "Length L:"+str(L)
print "ragelist:"+str(rangeList)
for key in strDict.keys():
    if strDict[key] >= output:
        output = strDict[key];
        print key, 'length:',strDict[key]

print "biggest M:"+str(biggestM)
newOut = 0;
for key in newStrDict.keys():
    if newStrDict[key] >= newOut:
        newOut = newStrDict[key];
        print key, 'length:',newStrDict[key]