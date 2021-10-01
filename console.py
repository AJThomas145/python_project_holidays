import pdb
from models.attraction import Attraction
from models.country import Country
from models.theme_park import Theme_park

import repositories.attraction_repository as attraction_repository 
import repositories.country_repository as country_repository
import repositories.theme_park_repository as theme_park_repository


country1 = Country("USA", "North America")
country_repository.save(country1)

attraction1 = Attraction("Space Mountain", "Thrill Ride")
attraction_repository.save(attraction1)

# theme_park1 = Theme_park('walt', attraction1, country1)
# theme_park_repository.save(theme_park1)


pdb.set_trace()