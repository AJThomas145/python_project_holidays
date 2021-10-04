from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.attraction_controller import attractions
from models.theme_park import Theme_park
import repositories.theme_park_repository as theme_park_repository
import repositories.attraction_repository as attraction_repository
import repositories.country_repository as country_repository

theme_parks_blueprint = Blueprint("theme_parks", __name__)

@theme_parks_blueprint.route("/home")
def Home():
    return render_template("index.html")

@theme_parks_blueprint.route("/theme_parks")
def theme_parks():
    theme_parks = theme_park_repository.select_all()
    return render_template("theme_parks/index.html", theme_parks = theme_parks)


@theme_parks_blueprint.route("/theme_parks/new")
def new_theme_park():
    countries = country_repository.select_all()
    theme_parks = theme_park_repository.select_all()
    return render_template("theme_parks/new.html", countries = countries, theme_parks = theme_parks)

@theme_parks_blueprint.route("/theme_parks", methods=["POST"])
def create_theme_park():
    name = request.form["name"]
    country_id = request.form["country_id"]
    visited = request.form["visited"]
    country = country_repository.select(country_id)
    theme_park = Theme_park(name, country, visited)
    theme_park_repository.save(theme_park)
    return redirect("/theme_parks")

@theme_parks_blueprint.route("/theme_parks/<id>/edit")
def edit_theme_park(id):
    theme_park = theme_park_repository.select(id)
    countries = country_repository.select_all()
    return render_template("theme_parks/edit.html", countries = countries, theme_park=theme_park)

@theme_parks_blueprint.route("/theme_parks/<id>/edit", methods=["POST"])
def update_theme_park(id):
    name = request.form["name"]
    country_id = request.form["country_id"]
    visited = request.form["visited"]
    country = country_repository.select(country_id)
    theme_park = Theme_park(name, country, visited, id)
    theme_park_repository.update(theme_park)
    return redirect("/theme_parks")

@theme_parks_blueprint.route("/theme_parks/<id>/delete", methods=["POST"])
def theme_park_delete(id):
    theme_park_repository.delete(id)
    return redirect("/theme_parks")