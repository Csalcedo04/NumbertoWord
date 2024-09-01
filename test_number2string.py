import unittest
from number2string import NumbertoWord, NumberOutOfRangeException

class TestNumberToWords(unittest.TestCase):
    
    def setUp(self):
        self.converter = NumbertoWord()  # Crear una instancia de NumberToWords para usar en las pruebas
    
    def test_single_digit(self):
        self.assertEqual(self.converter.number2string(5), "Five")
    
    def test_teens(self):
        self.assertEqual(self.converter.number2string(13), "Thirteen")
    
    def test_tens(self):
        self.assertEqual(self.converter.number2string(42), "Forty Two")
    
    def test_hundreds(self):
        self.assertEqual(self.converter.number2string(300), "Three Hundred")
    
    def test_large_numbers(self):
        self.assertEqual(self.converter.number2string(1000000), "One Million")
    def negative_numbers(self):
        self.assertEqual(self.converter.number2string(-3,506,847), "Minus 3 Million Five Hundred Six Eight Hundred Fourty Seven")
    def test_number_out_of_range(self):
        with self.assertRaises(NumberOutOfRangeException):
            self.converter.number2string(10**33)  # Un número más allá de decillones

# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
