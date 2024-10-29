#unwinding recursive calls --> Each level of the function can only complete and return its value once the next, smaller level has returned.

def get_kmers(n: int):
    """
    Function that generates all possible k-mers of a given length
    """
    nucleotides = ['A', 'T', 'C', 'G']
    if n == 1:
        return nucleotides
    
    sub_sequences = get_kmers(n-1)
    
    sequences = []
    
    for sequence in sub_sequences:
        for nucleotide in nucleotides:
            sequences.append(nucleotide + sequence)
    
    return sequences

print((get_kmers(2)))