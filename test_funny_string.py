import unittest

from funny_string import is_funny_string

class TestFunnyString(unittest.TestCase):
    def test_funny_string(self):
        self.assertEqual(is_funny_string("acxz"), "Funny")
        self.assertEqual(is_funny_string("bcxz"), "Not Funny")
        self.assertEqual(is_funny_string("abcd"), "Funny")
        self.assertEqual(is_funny_string("aaaa"), "Funny")
        self.assertEqual(is_funny_string("abba"), "Funny")
        self.assertEqual(is_funny_string("ivvkxq"), "Not Funny")
        self.assertEqual(is_funny_string("xxyy"), "Funny")
        self.assertEqual(is_funny_string("ivvkx"), "Not Funny")
        self.assertEqual(is_funny_string("a"), "Funny")

if __name__ == "__main__":
    unittest.main()