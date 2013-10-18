# string we are analyzing
if {[file exists ../genome.txt] && 1==1} {
	set genomefile [open ../genome.txt r]
	set strVal [read $genomefile]
	close $genomefile
	puts "Genome File Found!"
} else {
	set strVal "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
}
# L = length of string
# t = how many times it repeats
# codon size we are looking at (k-mer length)
set k 9
set t 3
set l 500
# true size
set kMod [expr $k - 1]

set runtimeStart [clock seconds]

# String Length
set strLength [string length $strVal]

set returnList ""
set strFirst ""
set ::rangeList ""

for {set i 0} { $i < $strLength-$k} {incr i} {
	
	# This gets the $k length character string desired
	set strRange [string range $strVal $i [expr $i + $kMod]]
	# count all matching strings
	set regexpCount [regexp -all $strRange [string range $strVal $i+1 $i+$l]]
	#puts "$strRange:$regexpCount"
	if {$regexpCount >= $t && [string length $strRange] == $k && [lsearch $::rangeList $strRange] == -1} {
		lappend ::rangeList $strRange
		#puts "$strRange:$regexpCount"
	}
}

set runtimeEnd [clock seconds]

puts "Length: $strLength
rangeList: $::rangeList
rangeList Length: [llength $::rangeList]
runtimeStart: $runtimeStart
runtimeEnd: $runtimeEnd
runtime: [expr $runtimeEnd - $runtimeStart]"
