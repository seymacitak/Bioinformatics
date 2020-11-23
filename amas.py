
protein = input("enter a protein: ")
amino_acid = input("enter an amino acid: ")
for i in range(len(protein)):
    if protein [i] in amino_acid:
        print("protein contains amino acis %s at position %s"%(protein[i],i))