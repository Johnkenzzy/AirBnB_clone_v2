#!/usr/bin/python3
"""
Flask web application to display states and their cities
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Fetches all states and their linked cities, then renders in template"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
