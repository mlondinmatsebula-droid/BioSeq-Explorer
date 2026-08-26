from .gc_analysis import gc_content, length

def summary_statistics(sequences):
    if not sequences:
        return {}
    gcs = [gc_content(seq) for seq in sequences.values()]
    lengths = [len(seq) for seq in sequences.values()]
    stats = {
        'average_gc': sum(gcs) / len(gcs),
        'longest_gene': max(lengths),
        'shortest_gene': min(lengths),
        'highest_gc': max(gcs),
        'lowest_gc': min(gcs),
    }
    return stats