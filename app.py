from flask import Flask, render_template

from controllers.attraction_controller import attractions_blueprint
from controllers.country_controller import countries_blueprint
from controllers.theme_park_controller import theme_parks_blueprint

app = Flask(__name__)

app.register_blueprint(attractions_blueprint)
app.register_blueprint(countries_blueprint)
app.register_blueprint(theme_parks_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)