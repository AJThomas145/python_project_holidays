from db.run_sql import run_sql

from models.attraction import Attraction
from models.country import Country
from models.theme_park import Theme_park

def save(attraction):
    sql = "INSERT INTO attractions (name, category) VALUES (%s, %s) RETURNING *"
    values = [attraction.name, attraction.category]
    results= run_sql(sql, values)
    id = results[0]["id"]
    attraction.id = id
    return attraction