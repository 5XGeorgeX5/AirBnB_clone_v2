#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(exception):
    "close storage"
    storage.close()


@app.route('/hbnb_filters')
def hbnb():
    "displays a HTML page"
    return render_template(
        '10-hbnb_filters.html',
        states=storage.all(State).values(),
        amenities_list=storage.all(Amenity).values()
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
