import unittest
from src.gc_analysis import gc_content, at_content, base_frequencies

class TestGC(unittest.TestCase):
    def test_gc(self):
        seq = "ATGC"
        self.assertAlmostEqual(gc_content(seq), 50.0)
        self.assertAlmostEqual(at_content(seq), 50.0)
        freqs = base_frequencies(seq)
        self.assertEqual(freqs['A'], 25.0)
        self.assertEqual(freqs['T'], 25.0)
        self.assertEqual(freqs['G'], 25.0)
        self.assertEqual(freqs['C'], 25.0)

if __name__ == '__main__':
    unittest.main()