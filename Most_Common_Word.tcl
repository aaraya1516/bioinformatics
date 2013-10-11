# string we are analyzing
set strVal "TAGGCAATATTCAGTATTCAGGGCCTTCTAATGCATATTCAGTAATGCAGTGGGAATATAGGCAATATTCAGGTGGGAATAGGCCTTCTATTCAGTAGGCAATAATGCATAGGCAATAGGCAATAATGCATAATGCATAATGCAGGCCTTCGTGGGAATAGTGGGAATAGGCCTTCGGCCTTCGGCCTTCTAATGCATAATGCAGGCCTTCGGCCTTCTATTCAGGGCCTTCGGCCTTCTAATGCAGTGGGAATAGTGGGAATATATTCAGGTGGGAATATAGGCAATAATGCATATTCAGGTGGGAATATAATGCATAATGCAGTGGGAATATAATGCATATTCAGTAGGCAAGGCCTTCTAGGCAATATTCAGGTGGGAATAGTGGGAATATATTCAGGGCCTTCGGCCTTCGGCCTTCTAATGCAGGCCTTCTATTCAGTAATGCAGTGGGAATAGTGGGAATATAGGCAATATTCAGTAGGCAATATTCAGTATTCAGGTGGGAATATAGGCAAGTGGGAATATAGGCAAGTGGGAATATATTCAGGTGGGAATAGGCCTTCGTGGGAATATAATGCATATTCAGTATTCAGGGCCTTCGGCCTTCTAGGCAAGTGGGAATAGGCCTTCTAATGCAGGCCTTCTATTCAGGTGGGAATATAATGCATAGGCAATAATGCATAATGCAGGCCTTCTAGGCAATATTCAGGTGGGAATAGTGGGAATATAATGCATAGGCAATATTCAGTAATGCATAATGCATAATGCATAGGCAATATTCAGTATTCAGGGCCTTCTATTCAGTATTCAGGTGGGAATATAATGCAGGCCTTCGTGGGAATAGTGGGAATATATTCAGTAATGCATAGGCAA"
# codon size we are looking at
set desiredLength 11
# true size
set desiredLengthMod [expr $desiredLength - 1]

set runtimeStart [clock seconds]

# String Length
set strLength [string length $strVal]

# Does it match a known start ATGATCAAG
set atga "ATGATCAAG"
set atgaMatch [string match -nocase $atga $strVal]

# Does it match a known stop ATGATCAAG
set cttg "CTTGATCAT"
set cttgMatch [string match -nocase $cttg $strVal]

set returnList ""
set strFirst ""
set ::rangeList ""

for {set i 0} { $i < $strLength} {incr i} {
	
	# This gets the 11 character string desired
	set strRange [string range $strVal $i [expr $i + $desiredLengthMod]]
	#set strFirst [string first $strRange $strVal $i]
	set regexpCount [regexp -all $strRange [string range $strVal $i+1 end]]
	
	# the ten is an arbitrary min times of repetition
	if {$regexpCount >= 8 && [string length $strRange] == $desiredLength && [lsearch $::rangeList $strRange] == -1} {
		lappend ::rangeList $strRange
		puts "$strRange:$regexpCount"
	}
}
set runtimeEnd [clock seconds]

puts "Length: $strLength
ATGA Match: $atgaMatch
CTTG Match: $cttgMatch
rangeList: $::rangeList
runtimeStart: $runtimeStart
runtimeEnd: $runtimeEnd
runtime: [expr $runtimeEnd - $runtimeStart]"
