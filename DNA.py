"""
  This program reads a genome file in a particular format and creates a 
  dictionary of bases with the count as the value.

  Author:    K. Holcomb
  Changelog: 2016-06-02 Initial version
"""

bases='ATCG'

def countBases(DNA):
    DNAcounts={'A':0,'T':0,'C':0,'G':0}
    for base in DNA:
        if base in bases:
            DNAcounts[base]+=1
    return DNAcounts

def printBaseComposition(DNAcounts):
     total=float(DNAcounts['A']+DNAcounts['T']+DNAcounts['C']+DNAcounts['G'])

     for base in bases:
         print "%s:%.2f" % (base,DNAcounts[base]/total)


fin=open('HIV.txt','r')

data=fin.readlines()

values=[]
for line in data:
    values.append(line.rstrip('\r\n').split()[1])

DNA="".join(values)

DNAcounts=countBases(DNA)
printBaseComposition(DNAcounts)
