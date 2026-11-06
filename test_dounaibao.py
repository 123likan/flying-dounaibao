"""运行：python3 -m unittest discover -s tests -v。"""
import unittest
from dounaibao import fly, pour_soymilk


class DounaibaoTest(unittest.TestCase):
    def test_flight_height(self):
        self.assertIn("30", fly(30))
        with self.assertRaises(ValueError):
            fly(0)

    def test_pour_conserves_liquid(self):
        for amount in [1, 100, 200, 333]:
            result = pour_soymilk(amount)
            self.assertEqual(result.served_ml + result.spilled_ml, amount)

    def test_invalid_pour(self):
        with self.assertRaises(ValueError):
            pour_soymilk(0)


if __name__ == "__main__":
    unittest.main()
