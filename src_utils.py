def complement_base(base):
    comp = {'A':'T','T':'A','C':'G','G':'C','N':'N'}
    return comp.get(base, 'N')

def is_dna(seq):
    return set(seq).issubset({'A','C','G','T','N'})