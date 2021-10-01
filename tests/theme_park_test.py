import unittest
from models.theme_park import Theme_park

class TestTheme_park(unittest.TestCase):

    def setUp(self):
        self.theme_park = Theme_park("Walt Disney World", "Space Mountain", "USA")


    def test_theme_park_has_name(self):
        self.assertEqual("Walt Disney World", self.theme_park.name)


    def test_theme_park_has_attraction(self):
        self.assertEqual("Space Mountain", self.theme_park.attraction)
        

    def test_theme_park_has_country(self):
        self.assertEqual("USA", self.theme_park.country)


    def test_theme_park_has_visited_starts_false(self):
        self.assertEqual(False, self.theme_park.visited)