def find_orfs(dna, min_length=30):
    """
    Find all open reading frames (start codon ATG to stop codon).
    Returns list of (start_pos, end_pos, sequence, frame).
    """
    orfs = []
    for frame in range(3):
        seq = dna[frame:]
        i = 0
        while i < len(seq) - 2:
            if seq[i:i+3] == 'ATG':
                start = i
                for j in range(i, len(seq) - 2, 3):
                    codon = seq[j:j+3]
                    if codon in ('TAA', 'TAG', 'TGA'):
                        end = j + 3
                        orf_seq = seq[start:end]
                        if len(orf_seq) >= min_length:
                            orfs.append((frame + start, frame + end, orf_seq, frame))
                        i = j + 3
                        break
                else:
                    break
            i += 1
    return orfs
