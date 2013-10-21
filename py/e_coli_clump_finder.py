#
#
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

# L = length of Frame
# t = how many times it repeats
# codon size we are looking at (k-mer length)
k = 9
t = 3
#subtract 1 since we start the count at 0
L = 500

epoch_timeStart = int(time.time())

strLength = len(genomeStr)

rangeList = [];

concatString = ""

i = 0
print "Starting Loop"
while (i <= strLength-k):
    # count 1 plus k-mer length
    endRange = i+k
    #value of string 
    strRange = genomeStr[i:endRange]

    if len(strRange) == k and genomeStr.count(strRange, i, i+L) >= t and strRange not in rangeList:
        rangeList.append(strRange)
        #concatString=concatString+" "+strRange
        #print "String: "+strRange
        #print "Count: "+str(genomeStr.count(strRange, i, i+L))

    i=i+1

print "Loop Ended"
epoch_timeEnd = int(time.time())

print "Length:"+str(strLength)
#print "ConcatString:"+concatString
#print "rangeList:"+str(rangeList)
print "rangeList Length:"+ str(len(rangeList))
print "runtimeStart:"+str(epoch_timeStart)
print "runtimeEnd:"+str(epoch_timeEnd)
print "runtime:"+str(epoch_timeEnd-epoch_timeStart)