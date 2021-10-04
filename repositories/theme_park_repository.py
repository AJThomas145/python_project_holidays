from db.run_sql import run_sql

from models.attraction import Attraction
from models.country import Country
from models.theme_park import Theme_park
import repositories.attraction_repository as attraction_repository
import repositories.country_repository as country_repository

def save(theme_park):
    sql = "INSERT INTO theme_parks (name, country_id, attraction_id, visited) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [theme_park.name, theme_park.country.id, theme_park.attraction.id, theme_park.visited]
    results = run_sql(sql, values)
    id = results[0]["id"]
    theme_park.id = id
    return theme_park

def delete_all():
    sql = "DELETE FROM theme_parks"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM theme_parks WHERE ID = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    theme_parks = []

    sql = "SELECT * FROM theme_parks"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row["country_id"])
        attraction = attraction_repository.select(row["attraction_id"])
        theme_park = Theme_park(row["name"], country, attraction, row["visited"], row["id"])
        theme_parks.append(theme_park)
    return theme_parks

def select(id):
    theme_park = None
    sql = "SELECT * FROM theme_parks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result["country_id"])
        attraction = attraction_repository.select(result["attraction_id"])
        theme_park = Theme_park(result["name"], country, attraction, result["visited"], result["id"])
    return theme_park

def update(theme_park):
    sql = "UPDATE theme_parks SET (name, country_id, attraction_id, visited) = (%s, %s, %s, %s) WHERE id = %s"
    values = [theme_park.name, theme_park.country.id, theme_park.attraction.id, theme_park.visited, theme_park.id]
    print(values)
    run_sql(sql, values)
