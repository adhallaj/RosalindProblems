sequence = "CAAGTCTTTATAGGAACAGTGCATGGTCCCGGAAGTCGGCCGGTATCGGCCTCAATAGACGATGGGTTACCCACACGTGTATGTGAGATAGATGCCTGAGGATATACGGTTAGTGCACCAATGACTGGGAAACATAGATTTGCGCCGCGCCGATTACGTCGAATCACTGAGCCGTTGGACCCTACGTATGGGATGGCTTAGAATCTGTGAGACTATACTTATTAGTGACTTCTTTGATATTCGCTTCCAACAGGCCAAGTTTCAGAAGAAACGAGACCGCTCATGTAATCGCGGGCAGTCATATCCTCTTGCAGGTGAAGGTAATCGGGATACCACGTCTGGATTCTCAGACTAAACCAGGCGTGAGTGACACTACTAGGCCTTGATCTCCGGCCGTCGAAGCTATTGGTCGGCACTGGACCTTGACAAGTTCTTCGGATCGGATTGTCGAAAAGGAGTCGGCGCCGAATCGTGATGAAAGTAAGCGCGCGATCGTCCCTAGCCGAAAAAAGGCAGGTGCATGAGGAAAGAGCTACGCTCTCCTTACAGGTTTGCATTAGACGTAAGGTGCTATCGTCTCTGCCAAACATAGGGGGAGGATGTGTCAGGCAATTAGGCTCGTCTATGCTTCAGTGTTGGCAGTCCTCTAGTTGGCACAAGAGTCCGTCGCTGCAGTTCTCTTCGGAAGTTTGAGGCATTAAATCTTCATGATGTACCTCCGTCCCGTAGCGGGCACTCTCATTTATAACAAGACGGGCTCTCACTCGTATTGTACGCCTAACTGATAGGGTCAGCCCCCTAGGACCTAAAAGAACCCCATCGCTGTGTTCTAACATCGCTTAACATCCCCAACTGGCGAGTGTTAGCCATCATGCATTCCTTTAGGAGACCCCGGAAGCTACTAGATGATCTGAGCTATCTAAACTACCATTCGCCGGGCCATCCGGACATTCTTTGAGTATATCCATGGCCGGAGCGTGCA"
A = 0
T = 0
C = 0
G = 0
for nucleotide in sequence:
    if nucleotide == "A":
        A = A + 1
    elif nucleotide == "T":
        T = T + 1
    elif nucleotide == "C":
        C = C + 1
    elif nucleotide == "G":
        G = G + 1
print(A, T, C, G)