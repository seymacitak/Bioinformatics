def gc_perc(): 
    dna = input("enter a dna: ")
    dna = dna.upper()
    gcpercent = float((dna.count("C") + dna.count("G")) * 100.0/len(dna))
    print(gcpercent)

def at_perc():
    dna = input("enter a dna: ")
    dna = dna.upper()
    atpercent = float((dna.count("A") + dna.count("T")) * 100.0/len(dna))
    print(atpercent)

def perc_count():

    print("1.Percent of gc in the dna sequence\n2.Percent of ta in the dna sequence")
    step = input("Number of the process you want to do: ")

    if step == "1": 
        gc_perc()
    
    elif step == "2":
        at_perc()

    else:
        print("error")

perc_count()
