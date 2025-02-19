#!/usr/bin/python3
"""
Flask web application to display States and Cities
"""
from flask import Flask, render_template
from models import storage, State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Displays all states sorted by name"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Displays a specific state and its cities"""
    states = storage.all(State)
    state = states.get(f"State.{id}")
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
