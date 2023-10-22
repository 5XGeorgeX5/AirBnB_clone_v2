#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(exception):
    "close storage"
    storage.close()


@app.route('/states')
def state():
    "displays a HTML page"
    return render_template('7-states_list.html', states=storage.all(State))


@app.route('/states/<id>')
def state_id(id):
    "displays a HTML page"
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
