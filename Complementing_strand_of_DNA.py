sequence = input('Input sequence: ')
complementaryseq = []

for nucleotide in sequence:
    if nucleotide == 'A':
        complementaryseq.append('T') # add items to end of lists using listname.append()
    elif nucleotide == 'T':
        complementaryseq.append('A')
    elif nucleotide == 'C':
        complementaryseq.append('G')
    elif nucleotide == 'G':
        complementaryseq.append('C')
    continue

complementaryseq.reverse() # listname.reverse() function reverses the list order

compseqstring = ""

for nucleotide in complementaryseq:
    compseqstring += nucleotide # += adds each iteration into the empty string above (compseqstring)

print('Your complimentary DNA sequence is', compseqstring)
