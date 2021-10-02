import pdb
from models.attraction import Attraction
from models.country import Country
from models.theme_park import Theme_park

import repositories.attraction_repository as attraction_repository 
import repositories.country_repository as country_repository
# import repositories.theme_park_repository as theme_park_repository

# theme_park_repository.delete_all()
attraction_repository.delete_all()
country_repository.delete_all()


country1 = Country("USA", "North America")
country_repository.save(country1)

country2 = Country("Japan", "Asia")
country_repository.save(country2)

attraction1 = Attraction("Space Mountain", "Thrill Ride")
attraction_repository.save(attraction1)

attraction2 = Attraction("Air Grover", "Family ride")
attraction_repository.save(attraction2)

# attraction1 = Attraction("Tower of Terror", "Thrill Ride")
# attraction_repository.update(attraction1)

# theme_park1 = Theme_park("Walt Disney World", country1, attraction1)
# theme_park_repository.save(theme_park1)

# theme_park2 = Theme_park("Busch Gardens", country1, attraction2)
# theme_park_repository.save(theme_park2)


pdb.set_trace()