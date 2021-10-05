import pdb
from models.attraction import Attraction
from models.country import Country
from models.theme_park import Theme_park

import repositories.attraction_repository as attraction_repository 
import repositories.country_repository as country_repository
import repositories.theme_park_repository as theme_park_repository

attraction_repository.delete_all()
theme_park_repository.delete_all()
country_repository.delete_all()


country1 = Country("USA", "North America")
country_repository.save(country1)

country2 = Country("Japan", "Asia")
country_repository.save(country2)

country3 = Country("Germany", "Europe")
country_repository.save(country3)

theme_park1 = Theme_park("Walt Disney World", country1)
theme_park_repository.save(theme_park1)

theme_park2 = Theme_park("Busch Gardens", country2)
theme_park_repository.save(theme_park2)

theme_park3 = Theme_park("Phantasialand", country3)
theme_park_repository.save(theme_park3)

attraction1 = Attraction("Space Mountain", "Thrill Ride", theme_park1)
attraction_repository.save(attraction1)

attraction2 = Attraction("Air Grover", "Family ride", theme_park2)
attraction_repository.save(attraction2)

attraction3 = Attraction("Rollercoaster", "Family ride", theme_park3)
attraction_repository.save(attraction3)

pdb.set_trace()