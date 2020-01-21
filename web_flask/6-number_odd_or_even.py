#!/usr/bin/python3
from flask import Flask, render_template
""" This is a Hello world code with different routes """


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Prints Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text=None):
    """ Prints with a parameter"""
    txt = text.replace('_', ' ')
    return 'C {}'.format(txt)


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ Prints with a parameter"""
    txt = text.replace('_', ' ')
    return 'Python {}'.format(txt)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Prints with a parameter"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Render a template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Render a template"""
    even_or_odd = "odd"
    if n % 2 == 0:
        even_or_odd = "even"
    return render_template('6-number_odd_or_even.html', n=n, even_or_odd=even_or_odd)


if __name__ == '__main__':
    app.run()
