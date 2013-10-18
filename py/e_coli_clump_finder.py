#
#
#
#


from os import path, access, R_OK  # W_OK for write permission.
import time

PATH='../genome.txt'

if path.isfile(PATH) and access(PATH, R_OK):
    print "Genome File Found!"
    #open the file
    genomeFile = open(PATH ,"r")
    genomeStr = genomeFile.read();
    genomeFile.close();
    #print "String:", genomeStr
else:
    print "Either file is missing or is not readable"

# L = length of string
# t = how many times it repeats
# codon size we are looking at (k-mer length)
k = 9
t = 3
L = 500
# true size
kMod = k - 1;

epoch_timeStart = int(time.time())

strLength = len(genomeStr)

strFirst = ""

rangeList = [];

i = 0
print "Starting Loop"
while (i < strLength-k):
	endRange = i+k
	strRange = genomeStr[i:endRange]
	#print strRange
	#print rangeList
	
	if genomeStr.count(strRange, i, i+L) >= 3 and (strRange not in rangeList):
		rangeList.append(strRange)
		#print strRange
		
	i=i+1

print "Loop Ended"
epoch_timeEnd = int(time.time())

print "Length:"+str(strLength)
print "rangeList:"+str(rangeList)
print "rangeList Length:"+ str(len(rangeList))
print "runtimeStart:"+str(epoch_timeStart)
print "runtimeEnd:"+str(epoch_timeEnd)
print "runtime:"+str(epoch_timeEnd-epoch_timeStart)