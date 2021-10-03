from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("/countries/index.html", countries = countries)

@countries_blueprint.route("/new")
def new_country():
    countries = country_repository.select_all()
    return render_template("new.html", countries=countries)

@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    name = request.form["name"]
    continent = request.form["continent"]
    country = Country(name, continent)
    country_repository.save(country)
    return redirect("/countries")

