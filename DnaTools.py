import collections

Nucleotides = ["A","T","G","C"]

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
        return tmpseq

def countNucFrequency(seq):
    tempFreqDict = {"A": 0, "T": 0, "G": 0, "C": 0}
    for nuc in seq:
        tempFreqDict[nuc] += 1
    return tempFreqDict


dnastring = "TAGCTACGATCGA"
result = countNucFrequency(dnastring)
print(result)


