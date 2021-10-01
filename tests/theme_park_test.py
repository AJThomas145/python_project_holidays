import unittest
from models.theme_park import Theme_park

class TestTheme_park(unittest.TestCase):

    def setUp(self):
        self.theme_park = Theme_park("Walt Disney World", "Spae Mountain", "USA")

    def test_theme_park_has_name(self):
        self.assertEqual("Walt Disney World", self.theme_park.name)


    # def test_theme_park_has_name
    # def test_theme_park_has_name