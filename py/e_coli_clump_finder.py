#
#
#
#


from os import path, access, R_OK  # W_OK for write permission.

PATH='../genome.txt'

if path.isfile(PATH) and access(PATH, R_OK):
    print "Genome File Found!"
    #open the file
    genomeFile = open(PATH ,"r")
    genomeStr = genomeFile.read();
    genomeFile.close();
    print "String:", genomeStr
else:
    print "Either file is missing or is not readable"