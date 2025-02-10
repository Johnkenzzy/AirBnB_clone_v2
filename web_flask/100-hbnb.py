#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage, State, Amenity, Place


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays the HBNB main page with filters and places"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)
    places = sorted(storage.all(Place).values(), key=lambda p: p.name)

    return render_template(
            '100-hbnb.html', states=states,
            amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
