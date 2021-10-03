from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.theme_park import Theme_park
import repositories.theme_park_repository as theme_park_repository
import repositories.attraction_repository as attraction_repository
import repositories.country_repository as country_repository

theme_parks_blueprint = Blueprint("theme_parks", __name__)

@theme_parks_blueprint.route("/theme_parks")
def theme_parks():
    theme_parks = theme_park_repository.select_all()
    return render_template("theme_parks/index.html", theme_parks = theme_parks)