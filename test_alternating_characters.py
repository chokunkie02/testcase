import unittest
from alternating_characters import count_alternating_deletions

class TestAlternatingCharacters(unittest.TestCase):
    def test_all_same(self):
        self.assertEqual(count_alternating_deletions("AAAAA"), 4)
    
    def test_perfect_alternation(self):
        self.assertEqual(count_alternating_deletions("ABABAB"), 0)
    
    def test_mixed_cases(self):
        self.assertEqual(count_alternating_deletions("AAABBB"), 4)
        self.assertEqual(count_alternating_deletions("AABBAABB"), 4)
        self.assertEqual(count_alternating_deletions("ABBABBAA"), 3)
    
if __name__ == "__main__":
    unittest.main()