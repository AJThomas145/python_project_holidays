from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.attraction import Attraction
import repositories.attraction_repository as attraction_repository
import repositories.theme_park_repository as theme_park_repository

attractions_blueprint = Blueprint("attractions", __name__)

@attractions_blueprint.route("/attractions")
def attractions():
    attractions = attraction_repository.select_all()
    return render_template("attractions/index.html", attractions=attractions)

@attractions_blueprint.route("/attractions/new")
def new_attractions():
    attractions = attraction_repository.select_all()
    theme_parks = theme_park_repository.select_all()
    return render_template("attractions/new.html", attractions=attractions, theme_parks = theme_parks)

@attractions_blueprint.route("/attractions", methods=["POST"])
def create_attraction():
    name = request.form["name"]
    category = request.form["category"]
    theme_park_id = request.form["theme_park_id"]
    theme_park = theme_park_repository.select(theme_park_id)
    attraction = Attraction(name, category, theme_park)
    attraction_repository.save(attraction)
    return redirect("/theme_parks")

@attractions_blueprint.route("/attractions/<id>/edit")
def edit_attraction(id):
    attraction = attraction_repository.select(id)
    theme_parks = theme_park_repository.select_all()
    return render_template("attractions/edit.html", attraction=attraction, theme_parks=theme_parks)

@attractions_blueprint.route("/attractions/<id>/edit", methods=["POST"])
def update_attraction(id):
    name = request.form["name"]
    category = request.form["category"]
    theme_park_id = request.form["theme_park_id"]
    theme_park = theme_park_repository.select(theme_park_id)
    attraction = Attraction(name, category, theme_park, id)
    attraction_repository.update(attraction)
    return redirect("/theme_parks")

@attractions_blueprint.route("/attractions/<id>/delete", methods=["POST"])
def attraction_delete(id):
    attraction_repository.delete(id)
    return redirect("/theme_parks")









