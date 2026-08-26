def detect_mutations(seq1, seq2):
    """
    Compare two sequences and report SNPs, insertions, deletions.
    Returns dict with 'snps', 'insertions', 'deletions'.
    """
    i, j = 0, 0
    snps = []
    insertions = []
    deletions = []
    while i < len(seq1) and j < len(seq2):
        if seq1[i] == seq2[j]:
            i += 1
            j += 1
        else:
            if i+1 < len(seq1) and seq1[i+1] == seq2[j]:
                deletions.append((i, seq1[i]))
                i += 1
            elif j+1 < len(seq2) and seq1[i] == seq2[j+1]:
                insertions.append((j, seq2[j]))
                j += 1
            else:
                snps.append((i, seq1[i], seq2[j]))
                i += 1
                j += 1
    while i < len(seq1):
        deletions.append((i, seq1[i]))
        i += 1
    while j < len(seq2):
        insertions.append((j, seq2[j]))
        j += 1
    return {'snps': snps, 'insertions': insertions, 'deletions': deletions}