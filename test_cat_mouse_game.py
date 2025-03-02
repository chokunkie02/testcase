import unittest
from cat_mouse_game import determine_winner

class TestCatAndMouse(unittest.TestCase):
    def test_tie(self):
        self.assertEqual(determine_winner(1, 3, 2), "Mouse C")
    
    def test_cat_a_wins(self):
        self.assertEqual(determine_winner(5, 10, 6), "Cat A")
    
if __name__ == "__main__":
    unittest.main()