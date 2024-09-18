import unittest
from operations import som, sub, mult, div

class TestCalculator(unittest.TestCase):
    def test_som(self):
        self.assertEqual(som(10, 5), 15)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)

    def test_mult(self):
        self.assertEqual(mult(10, 5), 50)

    def test_div(self):
        self.assertEqual(div(10, 5), 2)
        self.assertEqual(div(10, 0), "Não se pode dividir por Zero!")

if __name__ == "__main__":
    unittest.main()
