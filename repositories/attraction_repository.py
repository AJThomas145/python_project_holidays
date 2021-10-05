from db.run_sql import run_sql

from models.attraction import Attraction
from models.country import Country
from models.theme_park import Theme_park
import repositories.theme_park_repository as theme_park_repository
import repositories.country_repository as country_repository

def save(attraction):
    sql = "INSERT INTO attractions (name, category, theme_park_id) VALUES (%s, %s, %s) RETURNING *"
    values = [attraction.name, attraction.category, attraction.theme_park.id]
    results= run_sql(sql, values)
    id = results[0]["id"]
    attraction.id = id
    return attraction


def delete_all():
    sql = "DELETE FROM attractions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM attractions where ID = %s"
    values = [id]
    run_sql(sql, values)


def select_all():
    attractions = []

    sql = "SELECT * FROM attractions"
    results = run_sql(sql)

    for row in results:
        theme_park = theme_park_repository.select(row["theme_park_id"])
        attraction = Attraction(row["name"], row["category"], theme_park, row["id"])
        attractions.append(attraction)
    return attractions

def select (id):
    attraction = None
    sql = "SELECT * FROM attractions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        theme_park = theme_park_repository.select(result["theme_park_id"])
        attraction = Attraction(result['name'], result['category'], theme_park, result['id'])
    return attraction

def update(attraction):
    sql = "UPDATE attractions SET (name, category, theme_park_id) = (%s, %s, %s) WHERE id = %s"
    values = [attraction.name, attraction.category, attraction.theme_park.id, attraction.id]
    print(values)
    run_sql(sql, values)

def attractions_by_theme_park_id(id):
    attractions = []
    sql = "SELECT * FROM attractions WHERE theme_park_id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    for row in results:
        attraction = Attraction(row["name"], row["category"], row["theme_park_id"], row["id"])
        attractions.append(attraction)
    return attractions

