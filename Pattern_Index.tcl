#
#
# Pattern Matching
# Outputs character index start counts at 0
#
#

set pattern "ATAT"
set genome "GATATATGCATATACTT"
set locArray1 ""
set lastLoc 0
set locationNow 0

for {set i 0} {$i < [expr [string length $genome] - [string length $pattern]] && $locationNow >= 0} {incr i} {
	# increment the starting location by the last index plus 1 so we don't look at the same value over and over again
	if {$lastLoc >= 0} {
		set lastLoc [expr $lastLoc+1]
	}
	set locationNow [string first $pattern $genome $lastLoc]
	# don't append the index if it isn't found
	if {$locationNow >= 0} {
		lappend locArray1 $locationNow
	}
	#puts "Current Location: $locationNow
	#Last Location: $lastLoc"
	
	set lastLoc $locationNow
	
}
	

#set quantity [regexp -all $pattern $genome]

puts "Index:$locArray1"