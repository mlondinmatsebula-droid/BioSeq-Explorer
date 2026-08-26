from .gc_analysis import gc_content, at_content, length, base_frequencies
from .transcription import transcribe
from .reverse_complement import reverse_complement
from .translation import translate
from .orf_finder import find_orfs
from .mutation_detector import detect_mutations
from .statistics import summary_statistics

def generate_report(sequences, mut_seq=None):
    lines = []
    lines.append("BioSeq Report")
    lines.append("=" * 50)
    lines.append("")
    
    stats = summary_statistics(sequences)
    lines.append("Global Statistics:")
    lines.append(f"  Number of genes: {len(sequences)}")
    lines.append(f"  Average GC%: {stats['average_gc']:.2f}")
    lines.append(f"  Longest gene: {stats['longest_gene']} bp")
    lines.append(f"  Shortest gene: {stats['shortest_gene']} bp")
    lines.append(f"  Highest GC%: {stats['highest_gc']:.2f}")
    lines.append(f"  Lowest GC%: {stats['lowest_gc']:.2f}")
    lines.append("")
    
    for seq_id, seq in sequences.items():
        lines.append(f"Gene: {seq_id}")
        lines.append("-" * 40)
        lines.append(f"  Length: {length(seq)} bp")
        lines.append(f"  GC%: {gc_content(seq):.2f}")
        lines.append(f"  AT%: {at_content(seq):.2f}")
        freqs = base_frequencies(seq)
        lines.append(f"  Base frequencies: A={freqs['A']:.1f}%, C={freqs['C']:.1f}%, G={freqs['G']:.1f}%, T={freqs['T']:.1f}%")
        lines.append(f"  Reverse complement: {reverse_complement(seq)[:50]}...")
        rna = transcribe(seq)
        lines.append(f"  RNA (first 50): {rna[:50]}...")
        prot = translate(seq)
        lines.append(f"  Protein (first 50): {prot[:50]}...")
        orfs = find_orfs(seq)
        lines.append(f"  Number of ORFs (min 30 nt): {len(orfs)}")
        if orfs:
            lines.append("  ORFs (start, end, frame):")
            for orf in orfs[:5]:
                lines.append(f"    {orf[0]}-{orf[1]} frame {orf[3]}: {orf[2][:30]}...")
        lines.append("")
        
        gc = gc_content(seq)
        if gc > 60:
            lines.append("  Interpretation: High GC content may indicate greater thermal stability.")
        elif gc < 40:
            lines.append("  Interpretation: Low GC content may indicate less thermal stability.")
        else:
            lines.append("  Interpretation: Moderate GC content.")
        lines.append("")
    
    if mut_seq and len(sequences) >= 2:
        seq_ids = list(sequences.keys())
        seq_a = sequences[seq_ids[0]]
        seq_b = sequences[seq_ids[1]]
        muts = detect_mutations(seq_a, seq_b)
        lines.append("Mutation Comparison:")
        lines.append(f"  Comparing {seq_ids[0]} vs {seq_ids[1]}")
        lines.append(f"  SNPs: {len(muts['snps'])}")
        for snp in muts['snps'][:10]:
            lines.append(f"    Position {snp[0]}: {snp[1]} -> {snp[2]}")
        lines.append(f"  Insertions: {len(muts['insertions'])}")
        lines.append(f"  Deletions: {len(muts['deletions'])}")
        lines.append("")
    
    return "\n".join(lines)