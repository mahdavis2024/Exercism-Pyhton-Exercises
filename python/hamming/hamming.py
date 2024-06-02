def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        # When the sequences being passed are not the same length.
        raise ValueError("Strands must be of equal length.")
    else:
        hamming = 0
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                hamming += 1
    return hamming
        
