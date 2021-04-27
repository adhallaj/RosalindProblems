file = open(input('Enter file name: '))
fasta = file.read()
newlinesremoval = fasta.replace('\n', '')
fastasplit = newlinesremoval.split('>')
del fastasplit[0] # first element in fastasplit was blank

fastanames = []
gcpercentages = []
for i in fastasplit:
    fastanames.append(i[0:13])
    gccount = int(i.count("G") + i.count("C"))
    seqlength = int(i.count("A") + i.count("T") + gccount)
    gccontent = (gccount/seqlength)*100
    gcpercentages.append(gccontent)

maxposition = int(gcpercentages.index(max(gcpercentages))) # finds position of max gc content in gcpercentages

print(fastanames[maxposition]) # prints fasta name that corresponds to max gccontent in gcpercentages
print(max(gcpercentages)) # this prints the largest value in a list
