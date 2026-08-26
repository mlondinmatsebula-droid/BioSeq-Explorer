import unittest
from src.mutation_detector import detect_mutations

class TestMutation(unittest.TestCase):
    def test_mutations(self):
        seq1 = "ATGCGT"
        seq2 = "ATGAGT"
        muts = detect_mutations(seq1, seq2)
        self.assertEqual(len(muts['snps']), 1)
        self.assertEqual(muts['snps'][0], (3, 'C', 'A'))

if __name__ == '__main__':
    unittest.main()
