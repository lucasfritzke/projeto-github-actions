import unittest
from main import soma, subtracao, multiplicacao, divisao

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)
        self.assertEqual(subtracao(0, 7), -7)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(3, 4), 12)
        self.assertEqual(multiplicacao(-2, 5), -10)

    def test_divisao(self):
        self.assertEqual(divisao(10, 2), 5)
        with self.assertRaises(ValueError):
            divisao(10, 0)

if __name__ == "__main__":
    unittest.main()