# string we are analyzing
if {[file exists genome.txt]} {
	set genomefile [open genome.txt r]
	set strVal [read $genomefile]
	close $genomefile
} else {
	set strVal "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
}
# L = length of string
# t = how many times it repeats
# codon size we are looking at (k-mer length)
set k 5
# true size
set kMod [expr $k - 1]

set runtimeStart [clock seconds]

# String Length
set strLength [string length $strVal]

set returnList ""
set strFirst ""
set ::rangeList ""

for {set i 0} { $i < $strLength} {incr i} {
	
	# This gets the $k length character string desired
	set strRange [string range $strVal $i [expr $i + $kMod]]
	#set strFirst [string first $strRange $strVal $i]
	set regexpCount [regexp -all $strRange [string range $strVal $i+1 end]]
	
	# the ten is an arbitrary min times of repetition
	if {$regexpCount == 4 && [string length $strRange] == $k && [lsearch $::rangeList $strRange] == -1} {
		lappend ::rangeList $strRange
		puts "$strRange:$regexpCount"
	}
}

puts "Length: $strLength
rangeList: $::rangeList"
