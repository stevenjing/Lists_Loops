#Processing DNA in a file

# open the input file
file = open("input.txt")

# open the output file
output = open("trimmed.txt", "w")

# go through the input file one line at a time
for dna in file:
    
    # get the substring from the 15th character to the end
    trimmed_dna = dna[14:]
    
    # print out the trimmed sequence
    output.write(trimmed_dna)
    
    # print out the length to the screen
    print("processed sequence with length " + str(len(trimmed_dna)))

#Multiple exons from genomic DNA


# open the genomic dna file and read the contents
genomic_dna = open("genomic_dna.txt").read()

# open the exons locations file
exon_locations = open("exons.txt")

# create a variable to hold the coding sequence
coding_sequence = ""

# go through each line in the exon locations file
for line in exon_locations:
    
    # split the line using a comma
    positions = line.split(',')
    
    # get the start and stop positions
    start = int(positions[0])
    stop = int(positions[1])
    
    # extract the exon from the genomic dna
    exon = genomic_dna[start:stop]
    
    # append the exon to the end of the current coding sequence
    coding_sequence = coding_sequence + exon
￼
# write the coding sequence to an output file
output = open("coding_sequence.txt", "w")
output.write(coding_sequence)
output.close()
