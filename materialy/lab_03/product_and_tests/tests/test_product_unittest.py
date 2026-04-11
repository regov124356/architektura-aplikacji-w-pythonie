# ========================================
# Szkielet pliku: test_product_unittest.py
# Uzupelnij metody testowe!
# ========================================


import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        # TODO: Stworz instancje Product, np. Product("Laptop", 2999.99, 10)
        self.product = Product("Laptop", 2999.99, 10)

    def test_add_stock_positive(self):
        # TODO: Wywolaj add_stock i sprawdz nowa wartosc quantity
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 15)

    def test_add_stock_negative_raises(self):
        # TODO: Uzyj self.assertRaises(ValueError)
        self.assertRaises(ValueError, self.product.add_stock, -3)

    def test_remove_stock_positive(self):
        # TODO: Wywolaj remove_stock i sprawdz quantity
        self.product.remove_stock(5)
        self.assertEqual(self.product.quantity, 5)

    def test_remove_stock_too_much_raises(self):
        # TODO: Uzyj self.assertRaises(ValueError)
        self.assertRaises(ValueError, self.product.remove_stock, 10)

    def test_is_available_when_in_stock(self):
        # TODO: Uzyj self.assertTrue
        self.assertTrue(self.product.is_available())

    def test_is_not_available_when_empty(self):
        # TODO: Stworz produkt z quantity=0, uzyj self.assertFalse
        empty_product = Product("Empty", 0.0, 0)
        self.assertFalse(empty_product.is_available())

    def test_total_value(self):
        # TODO: Uzyj self.assertEqual
        self.assertEqual(self.product.total_value(), 29999.9)


if __name__ == "__main__":
    unittest.main()


print("Uruchom testy komenda: python -m unittest test_product_unittest -v")