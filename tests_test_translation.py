import unittest
from src.translation import translate

class TestTranslation(unittest.TestCase):
    def test_translate(self):
        dna = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
        prot = translate(dna)
        self.assertEqual(prot, "MAIVMGR")
        self.assertEqual(translate(dna, start_codon=False), "MAIVMGR*")
        self.assertEqual(translate("TTT"), "")

if __name__ == '__main__':
    unittest.main()