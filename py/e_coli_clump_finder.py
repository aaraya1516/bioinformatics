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
while (i < strLength-k):
	endRange = i+k
	strRange = genomeStr[i:endRange]
	#print strRange
	#print rangeList
	
	if genomeStr.count(strRange, i, strLength) == 3 and (strRange not in rangeList):
		rangeList.append(strRange)
		print strRange

	i=i+1

epoch_timeEnd = int(time.time())

print "Length:"+strLength
print "rangeList:"+rangeList
print "rangeList Length:"+ len(rangeList)
print "runtimeStart:"+epoch_timeStart
print "runtimeEnd:"+epoch_timeEnd
print "runtime:"+epoch_timeEnd-epoch_timeStart