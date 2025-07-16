import unittest
from src.sweetshop import SweetShop

class TestSweetShop(unittest.TestCase):
    def test_add_sweet(self):
        shop = SweetShop()
        shop.add_sweet("Kaju Katli", "Nut-Based", 50, 20)
        self.assertEqual(len(shop.get_all_sweets()), 1)
