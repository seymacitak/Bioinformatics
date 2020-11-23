def gc_percent(): 
    dna = input("enter a dna: ")
    dna = dna.upper 
    bases = len(dna) 
    gc_percent = float(dna_seq.count("C")+ dna_seq.count("G"))*100.0/(len(dna_seq)-bases)
    
def at_percent(dna_seq) :
    dna_seq = input("enter a dna sequence: ")
    dna_seq = dna_seq.upper 
    bases = len(dna_seq)
    at_percent =  float(dna_seq.count("A")+ dna_seq.count("T"))*100.0/(len(dna_seq)-bases)

print("1.Percent of gc in the dna sequence\n2.Percent of ta in the dna sequence")
step = input("Number of the process you want to do: ")

if step == "1": 
    gc_percent()

else:
    at_percent()
