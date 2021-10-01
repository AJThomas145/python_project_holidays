from db.run_sql import run_sql

from models.attraction import Attraction
from models.country import Country
from models.theme_park import Theme_park
import repositories.attraction_repository as attraction_repository
import repositories.country_repository as country_repository

def save(theme_park):
    sql = "INSERT INTO theme_parks (name, country_id, attraction_id, visited) (%s, %s, %s, %s) RETURNING *"
    values = [theme_park.name, theme_park.country.id, theme_park.attraction.id, theme_park.visited]
    results = run_sql(sql, values)
    id = results[0]["id"]
    theme_park.id = id
    return theme_park