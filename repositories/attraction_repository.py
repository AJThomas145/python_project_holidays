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
        attraction = Attraction(row["name"], ["category"], row["id"])
        attractions.append(attraction)
    return attractions

def select (id):
    attraction = None
    sql = "SELECT * FROM attractions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        attraction = Attraction(result['name'], result['category'], result['id'])
    return attraction

def update(attraction):
    sql = "UPDATE attractions SET (name, category) = (%s, %s) WHERE id = %s"
    values = [attraction.name, attraction.category, attraction.id]
    print(values)
    run_sql(sql, values)

