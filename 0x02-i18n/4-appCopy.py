#!/usr/bin/env python3
'''Task 4: Force locale with URL parameter
'''

from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    '''Config class'''

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

# Define the get_locale function before initializing Babel
def get_locale() -> str:
    """Retrieves the locale for a web page.

    Returns:
        str: best match
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Babel()

# Initialize Babel with the app and locale_selector
babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def index() -> str:
    '''default route

    Returns:
        html: homepage
    '''
    return render_template("4-index.html")

if __name__ == "__main__":
    app.run(debug=True)
