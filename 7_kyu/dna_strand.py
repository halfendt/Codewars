def DNA_strand(dna):
    """
    Complementary DNA Kata
    https://www.codewars.com/kata/554e4a2f232cdd87d9000038
    """
    new_dna = ''
    for lett in dna:
        if lett == 'G':
            new_dna += 'C'
        elif lett == 'C':
            new_dna += 'G'
        elif lett == 'A':
            new_dna += 'T'
        elif lett == 'T':
            new_dna += 'A'
    return new_dna