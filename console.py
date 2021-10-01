import pdb
from models.attraction import Attraction
from models.country import Country
from models.theme_park import Theme_park

import repositories.attraction_repository as attraction_repository 
import repositories.country_repository as country_repository
import repositories.theme_park_repository as theme_park_repository


country1 = Country("USA", "North America")

attraction1 = Attraction("Space Mountain", "Thrill Ride")

theme_park1 = Theme_park("Walt Disney World", "Space Mountain", "USA")


pdb.set_trace()