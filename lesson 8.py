import unittest



def multiply(a, b):
    return a * b


# Тесты
class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(1, 10), 10)


if __name__ == '__main__':
    unittest.main()