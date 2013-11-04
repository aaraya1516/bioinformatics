#
# Skew Exercise
# the difference between the total number of occurrences of G and C in Genome
#


from os import path, access, R_OK  # W_OK for write permission.
import time

PATH='../skewgenome.txt'
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
    genomeStr = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"

epoch_timeStart = int(time.time())

strLength = len(genomeStr)

skewCnt = gCnt = cCnt = prevMinSkewCnt= 0
skewSet = [];
oriIndex = [];
i = 0

print "Starting Loop"
print "Genome Length:"+str(strLength);
while (i <= strLength-1):
    #value of string 
    strRange = genomeStr[i:i+1]
    # appends value to skewSet list
    skewSet.append(skewCnt);
    #print str(skewCnt);
    if strRange == "G":
        skewCnt=skewCnt+1
        gCnt=gCnt+1
    elif strRange == "C":
        skewCnt=skewCnt-1
        cCnt=cCnt+1
    i=i+1
    minSkewSet = min(skewSet)
    if skewCnt < minSkewSet:
        oriIndexLength = len(oriIndex);
        #print str(oriIndexLength);
        if oriIndexLength > 0 and skewCnt < minSkewSet:
            oriIndex.remove(str(prevMinSkewCnt));
            #print "What?"
        oriIndex.append(str(i))
        prevMinSkewCnt = i;

print "Loop Ended"
epoch_timeEnd = int(time.time())

print "Skew Sum:"+ str(skewCnt)
#print "Skew Set:"+str(skewSet)
print "OriC Index:" + str(oriIndex)
print "#G:"+str(gCnt)
print "#C:"+str(cCnt)
print "runtimeStart:"+str(epoch_timeStart)
print "runtimeEnd:"+str(epoch_timeEnd)
print "runtime:"+str(epoch_timeEnd-epoch_timeStart)