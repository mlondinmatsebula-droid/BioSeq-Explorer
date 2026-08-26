class SequenceDatabase:
    def __init__(self):
        self.data = {}

    def add_gene(self, seq_id, sequence):
        self.data[seq_id] = sequence

    def remove_gene(self, seq_id):
        if seq_id in self.data:
            del self.data[seq_id]

    def search_gene(self, query):
        results = {}
        for seq_id, seq in self.data.items():
            if query in seq:
                results[seq_id] = seq
        return results

    def get_all(self):
        return self.data.copy()

    def load_from_fasta(self, filepath):
        from .fasta_reader import load_fasta
        self.data.update(load_fasta(filepath))