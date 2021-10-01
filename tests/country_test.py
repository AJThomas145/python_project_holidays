import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country = Country("USA", "North America")

    def test_country_has_name(self):
        self.assertEqual("USA", self.country.name)

    def test_country_has_continent(self):
        self.assertEqual("North America", self.country.continent)