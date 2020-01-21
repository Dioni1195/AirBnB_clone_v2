#!/usr/bin/python3
from models import storage
from models.state import State
from flask import Flask, render_template
""" This module import data from storage """


@app.teardown_appcontext
def close(arg):
    """ Close the session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Lists the states """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run()
