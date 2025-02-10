#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage, State, Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays an HTML page with filters for States and Amenities"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)

    return render_template(
            '10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
