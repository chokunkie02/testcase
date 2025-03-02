import unittest
from longest_alternating_substring import find_longest_alternating_substring

class TestAlternate(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(find_longest_alternating_substring("beabeefeab"), 5)
        self.assertEqual(find_longest_alternating_substring("rryyzz"), 0)
        self.assertEqual(find_longest_alternating_substring("abababab"), 8)
    
if __name__ == "__main__":
    unittest.main()