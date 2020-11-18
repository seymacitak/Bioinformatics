def find_position():
    dna = input("Enter a sequence: ")
    dna = dna.upper()
    seq = input("Enter the sequence whose position you want to find: ")
    seq = seq.upper()
    pos = dna.find(seq, 0)

    while pos > -1 :
        print("atgc at position %s" %pos)
        pos = dna.find(seq, pos+1)

    
print(find_position())