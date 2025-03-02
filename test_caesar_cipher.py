import unittest
from caesar_cipher import apply_caesar_cipher

class TestCaesarCipher(unittest.TestCase):
    def test_shift_2(self):
        self.assertEqual(apply_caesar_cipher("middle-Outz", 2), "okffng-Qwvb")
    
    def test_shift_13(self):
        self.assertEqual(apply_caesar_cipher("Caesar-Cipher", 13), "Pnrfne-Pvcure")
    
    def test_non_alphabets(self):
        self.assertEqual(apply_caesar_cipher("123!@#", 5), "123!@#")
    
if __name__ == "__main__":
    unittest.main()