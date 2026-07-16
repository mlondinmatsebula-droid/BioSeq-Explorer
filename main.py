#!/usr/bin/env python3
import sys
import os
from src.fasta_reader import load_fasta
from src.sequence_database import SequenceDatabase
from src.report_generator import generate_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <fasta_file> [mutations_file]")
        sys.exit(1)
    
    fasta_file = sys.argv[1]
    mut_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    db = SequenceDatabase()
    db.load_from_fasta(fasta_file)
    sequences = db.get_all()
    
    mut_sequences = None
    if mut_file:
        mut_sequences = load_fasta(mut_file)
    
    report = generate_report(sequences, mut_sequences)
    print(report)
    
    os.makedirs('reports', exist_ok=True)
    with open('reports/analysis_report.txt', 'w') as f:
        f.write(report)
    print("\nReport saved to reports/analysis_report.txt")

if __name__ == "__main__":
    main()