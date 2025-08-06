def dna_translation(dna_strand):
    if dna_strand.lower() == 'g':
        return 'C'
    elif dna_strand.lower() == 'c':
        return 'G'
    elif dna_strand.lower() == 't':
        return 'A'
    elif dna_strand.lower() == 'a':
        return 'U'

    return dna_strand

def to_rna(dna_strand):
    if len(dna_strand) > 1:
        
        translated = ''
        for letter in dna_strand:
            translated += dna_translation(letter)
    
    else:
        translated = dna_translation(dna_strand)

    return translated