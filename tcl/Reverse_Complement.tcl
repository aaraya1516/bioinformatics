#
#
# Reverse Complement of genome
#
#


set genome "AGTCGCATAGT"

set rvrsGenome [string reverse $genome]

set complementGenome [string map {A T T A G C C G} $rvrsGenome]

puts "Reverse Complement of $genome
Is: $complementGenome"