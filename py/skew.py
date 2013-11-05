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

skewCnt =0;
gCnt =0;
cCnt = 0;
skewSet =[];
prevMinSkewCnt=[];
oriIndex = [];
inr = 0;

print "Starting Loop"
print "Genome Length:"+str(strLength);
while (inr <= strLength-1):
    #value of string 
    strRange = genomeStr[inr:inr+1]
    # appends value to skewSet list
    skewSet.append(skewCnt);
    #print str(skewCnt);
    if strRange == "G":
        skewCnt=skewCnt+1
        gCnt=gCnt+1
    elif strRange == "C":
        skewCnt=skewCnt-1
        cCnt=cCnt+1
    inr=inr+1
    minSkewSet = min(skewSet)
    #print "minSkewSet:"+str(minSkewSet)
    #print "skewCnt:"+str(skewCnt)
    if str(prevMinSkewCnt) != str(prevMinSkewCnt):
        print "prevMinSkewCnt:"+str(prevMinSkewCnt)

    if skewCnt <= minSkewSet:
        #oriIndexLength = len(oriIndex);
        #print str(oriIndexLength);
        if skewCnt < minSkewSet:
            for index in prevMinSkewCnt:
                oriIndex.remove(index);
                prevMinSkewCnt.remove(index);
            #print str(prevMinSkewCnt)
        oriIndex.append(inr)
        prevMinSkewCnt.append(inr);

print "Loop Ended"
epoch_timeEnd = int(time.time())

print "Skew Sum:"+ str(skewCnt)
#print "Skew Set:"+str(skewSet)
print "OriC Index:" + str(oriIndex)
print "Indexed Skew Sum:"
for index in oriIndex:
    print skewSet[index]
print "#G:"+str(gCnt)
print "#C:"+str(cCnt)
print "runtimeStart:"+str(epoch_timeStart)
print "runtimeEnd:"+str(epoch_timeEnd)
print "runtime:"+str(epoch_timeEnd-epoch_timeStart)