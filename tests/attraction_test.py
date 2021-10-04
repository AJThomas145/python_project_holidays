import unittest
from models.attraction import Attraction

class TestAttraction(unittest.TestCase):

    def setUp(self):
        self.attraction = Attraction("Space Mountain", "Thrill Ride", "Walt Disney World")

    def test_attraction_has_name(self):
        self.assertEqual("Space Mountain", self.attraction.name)

    def test_attraction_has_category(self):
        self.assertEqual("Thrill Ride", self.attraction.category)

    def test_theme_park_has_theme_park(self):
        self.assertEqual("Walt Disney World", self.attraction.theme_park)