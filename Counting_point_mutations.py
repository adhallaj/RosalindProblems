file = open(input("Enter file name: "))
readfile = file.read()
sequences = readfile.split("\n")
del sequences[2] # this is to get rid of relic item in sequences list

seqone = sequences[0]
seqtwo = sequences[1]

hammdistance = 0

for a, b in zip(seqone, seqtwo):
    if a != b:
        hammdistance += 1

print(hammdistance)
