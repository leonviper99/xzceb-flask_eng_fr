import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french(' '),' ')
        a = "Hello"
        b = "Bonjour"
        self.assertEqual(english_to_french(a),b)
        
class TestFrenchToEnglish(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(english_to_french(' '),' ')
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        
        
if __name__ == '__main__':
    unittest.main()