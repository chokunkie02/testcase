import unittest
from grid_validator import is_grid_sorted

class TestGridChallenge(unittest.TestCase):
    def test_sorted_grid(self):
        self.assertEqual(is_grid_sorted(["abc", "ade", "efg"]), "YES")
    
    def test_unsorted_grid(self):
        self.assertEqual(is_grid_sorted(["uxf", "vof", "hmp"]), "NO")
    
if __name__ == "__main__":
    unittest.main()