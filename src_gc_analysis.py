def gc_content(seq):
    if not seq:
        return 0.0
    gc = seq.count('G') + seq.count('C')
    return (gc / len(seq)) * 100

def at_content(seq):
    if not seq:
        return 0.0
    at = seq.count('A') + seq.count('T')
    return (at / len(seq)) * 100

def length(seq):
    return len(seq)

def base_frequencies(seq):
    freqs = {}
    total = len(seq)
    for base in 'ACGT':
        freqs[base] = (seq.count(base) / total) * 100 if total else 0
    return freqs