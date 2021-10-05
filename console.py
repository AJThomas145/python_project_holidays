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


country1 = Country("USA", "NORTH AMERICA")
country_repository.save(country1)

country2 = Country("JAPAN", "ASIA")
country_repository.save(country2)

country3 = Country("GERMANY", "EUROPE")
country_repository.save(country3)

country4 = Country("SOUTH KOREA", "ASIA")
country_repository.save(country4)

country5 = Country("AUSTRALIA", "OCEANIA")
country_repository.save(country5)

theme_park1 = Theme_park("WALT DISNEY WORLD", country1)
theme_park_repository.save(theme_park1)

theme_park2 = Theme_park("BUSCH GARDENS", country1)
theme_park_repository.save(theme_park2)

theme_park3 = Theme_park("UNIVERSAL STUDIOS", country2)
theme_park_repository.save(theme_park3)

theme_park4 = Theme_park("DISNEYSEA", country2)
theme_park_repository.save(theme_park4)

theme_park5 = Theme_park("EUROPA PARK", country3)
theme_park_repository.save(theme_park5)

theme_park6 = Theme_park("PHANTASIALAND", country3)
theme_park_repository.save(theme_park6)

theme_park7 = Theme_park("EVERLAND", country4)
theme_park_repository.save(theme_park7)

theme_park8 = Theme_park("LOTTE WORLD", country4)
theme_park_repository.save(theme_park8)

theme_park9 = Theme_park("DREAMWORLD", country5)
theme_park_repository.save(theme_park9)

theme_park10 = Theme_park("WARNER BROS MOVIE WORLD", country5)
theme_park_repository.save(theme_park10)

attraction1 = Attraction("SPACE MOUNTAIN", "THRILL RIDE", theme_park1)
attraction_repository.save(attraction1)

attraction2 = Attraction("BUZZ LIGHTYEAR", "FAMILY RIDE", theme_park1)
attraction_repository.save(attraction2)

attraction3 = Attraction("DUMBO THE FLYING ELEPHANT", "FAMILY RIDE", theme_park1)
attraction_repository.save(attraction3)

attraction4 = Attraction("MONTU", "THRILL RIDE", theme_park2)
attraction_repository.save(attraction4)

attraction5 = Attraction("AIR GROVER", "FAMILY RIDE", theme_park2)
attraction_repository.save(attraction5)

attraction6 = Attraction("SERENGETI EXPRESS", "FAMILY RIDE", theme_park2)
attraction_repository.save(attraction6)

attraction7 = Attraction("HOLLYWOOD DREAM", "THRILL RIDE", theme_park3)
attraction_repository.save(attraction7)

attraction8 = Attraction("ELMO'S LITTLE DRIVE", "FAMILY RIDE", theme_park3)
attraction_repository.save(attraction8)

attraction9 = Attraction("TERMINATOR 2", "THRILL RIDE", theme_park3)
attraction_repository.save(attraction9)

attraction10 = Attraction("TOWER OF TERROR", "THRILL RIDE", theme_park4)
attraction_repository.save(attraction10)

attraction11 = Attraction("TOY STORY MANIA", "FAMILY RIDE", theme_park4)
attraction_repository.save(attraction11)

attraction12 = Attraction("NEMO & FRIENDS", "FAMILY RIDE", theme_park4)
attraction_repository.save(attraction12)

attraction13 = Attraction("ARTHUR", "THRILL RIDE", theme_park5)
attraction_repository.save(attraction13)

attraction14 = Attraction("BA-A-A EXPRESS", "FAMILY RIDE", theme_park5)
attraction_repository.save(attraction14)

attraction15 = Attraction("BLUE FIRE MEGACOASTER", "THRILL RIDE", theme_park5)
attraction_repository.save(attraction15)

attraction16 = Attraction("FLYING LAUNCH COASTER", "THRILL RIDE", theme_park6)
attraction_repository.save(attraction16)

attraction17 = Attraction("FREE LIKE A BIRD", "FAMILY RIDE", theme_park6)
attraction_repository.save(attraction17)

attraction18 = Attraction("BLACK MAMBA", "THRILL RIDE", theme_park6)
attraction_repository.save(attraction18)

attraction19 = Attraction("T EXPRESS", "THRILL RIDE", theme_park7)
attraction_repository.save(attraction19)

attraction20 = Attraction("KIDS VILLAGE", "FAMILY RIDE", theme_park7)
attraction_repository.save(attraction20)

attraction21 = Attraction("SAFARI WORLD", "FAMILY RIDE", theme_park7)
attraction_repository.save(attraction21)

attraction22 = Attraction("ATLANTIS", "THRILL RIDE", theme_park8)
attraction_repository.save(attraction22)

attraction23 = Attraction("EUREKA", "FAMILY RIDE", theme_park8)
attraction_repository.save(attraction23)

attraction24 = Attraction("UNDER SEA KINGDOM", "FAMILY RIDE", theme_park8)
attraction_repository.save(attraction24)

attraction25 = Attraction("THE GOLD COASTER", "THRILL RIDE", theme_park9)
attraction_repository.save(attraction25)

attraction26 = Attraction("DREAMWORLD EXPRESS", "FAMILY RIDE", theme_park9)
attraction_repository.save(attraction26)

attraction27 = Attraction("THE CLAW", "THRILL RIDE", theme_park9)
attraction_repository.save(attraction27)

attraction28 = Attraction("DC RIVALS HYPERCOASTER", "THRILL RIDE", theme_park10)
attraction_repository.save(attraction28)

attraction29 = Attraction("LOONEY TUNES", "FAMILY RIDE", theme_park10)
attraction_repository.save(attraction29)

attraction30 = Attraction("DOOMSDAY DESTROYER", "THRILL RIDE", theme_park10)
attraction_repository.save(attraction30)

pdb.set_trace()