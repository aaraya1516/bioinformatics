#Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
#     Input: Two strings Pattern and Text along with an integer d.
#     Output: All positions where Pattern appears in Text with at most d mismatches.
#
#CODE CHALLENGE: Solve the Approximate Pattern Matching Problem
#
#Sample Input:
#     ATTCTGGA
#     CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
#     3
set runtimeStart [clock seconds]
# get string we are analyzing from genom
if {[file exists ../aprx_genome.txt]} {
	set genomefile [open ../genome.txt r]
	set gnomestr [read $genomefile]
	close $genomefile
	puts "Genome File Found!"
} else {
	set gnomestr "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
}
set gnmstrL [string length $gnomestr]
# Quantify permutations if allowed
set t 3
#What are we matching from?
set mtx_base "ATTCTGGA"
set mtx_l [string length $mtx_base]
	set strRange $mtx_base
	set gnmstrLmod [expr $t*[string length $gnomestr]]
	set kMod 0
	set k 0

if {$mtx_base == ""} {
	# k = k-mer length;  codon size we are looking at
	set k 9
	set kMod 0
	set gnmstrLmod [string length $gnomestr]-$k
}

#Are we looking in a frame?
# L = length of frame
if {0} {
	set L 500
} {
	set L $gnmstrL
}

set ::rangeList ""
set mtx_base_original $mtx_base
#
# Start Sorting through string
#
#for {set i 0} { $i < $gnmstrLmod} {incr i} {
for {set i 0} { $i < 2} {incr i} {
	set mtx_base $mtx_base_original
	#Do we have a mtx_base given?
	if {$mtx_base == ""} {
		#
		# Exact Pattern Matching
		#
		# This gets the $k length character string desired
		set strRange [string range $gnomestr $i [expr $i + $kMod]]
		# count all matching strings
		set regexpCount [regexp -all $strRange [string range $gnomestr $i+1 $i+$L]]
		#puts "$strRange:$regexpCount"
		if {$regexpCount >= $t && [string length $strRange] == $k && [lsearch $::rangeList $strRange] == -1} {
			lappend ::rangeList $strRange
			#puts "$strRange:$regexpCount"
		}
	} else {
		#
		#Approximate Pattern Matching
		#
		puts "i count:$i"
		set second 0
		set third 0
		set fourth 0
		for {set inc 0} {$inc <= [expr $mtx_l-[expr $t-2]]} {incr inc} {
			set mtx_base $mtx_base_original
			if {$i <1} {
				set mtx_base [string replace $mtx_base $inc $inc "."]
				incr second
				puts "Base:$mtx_base"
				#count mathing strings
				set matchCount [regexp -all $gnomestr $mtx_base]
				puts "Match Count:$matchCount"
			}
		}
		set mtx_base [string replace $mtx_base 0 0 "."]
				set mtx_new_base $mtx_base
				
				for {set in 1} {$in <= [expr $mtx_l-[expr $t-2]]} {incr in} {
					set mtx_base $mtx_new_base
					set mtx_base [string replace $mtx_base $in $in "."]
					puts "Base2:$mtx_base"
					#count mathing strings
					set matchCount [regexp -all $gnomestr $mtx_base]
					puts "Match2 Count:$matchCount"
				}
	}

}

set runtimeEnd [clock seconds]

puts "Length: $gnmstrL
second: $second
third: $third
fourth: $fourth
rangeList: $::rangeList
rangeList Length: [llength $::rangeList]
runtimeStart: $runtimeStart
runtimeEnd: $runtimeEnd
runtime: [expr $runtimeEnd - $runtimeStart]"