import unittest
from fizzbuzz_game import fizzbuzz_game

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz_game(15), "FizzBuzz")
        self.assertEqual(fizzbuzz_game(30), "FizzBuzz")
    
    def test_number(self):
        self.assertEqual(fizzbuzz_game(7), "7")
    
if __name__ == "__main__":
    unittest.main()