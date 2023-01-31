#!/usr/bin/env python3
'''Flask app babel setup'''
from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    '''Flask Babel configuraltion representation'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.locale_selector
def get_locale() -> str:
    '''Retrieve locale from webpage'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_index() -> str:
    '''Home page'''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
