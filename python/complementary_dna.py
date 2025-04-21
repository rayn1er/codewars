def DNA_strand(dna):
    # code here
    
   

    new_word = []
    
    for i in dna:
        if i == "A":
            new_word.append("T")
        elif i == "T":
            new_word.append("A")
        elif i == "G":
            new_word.append("C")
        elif i == "C":
            new_word.append("G")
        else:
            new_word.append(i)
        
    
    return ''.join(new_word)
    