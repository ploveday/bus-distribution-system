"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ABDS import app
from ABDS import assignRoute

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    deploying = assignRoute.assignRoute(assignRoute.location)
    return render_template(
        'index.html',
        title='Automated Bus Distribution System',
        deploying=deploying,
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    return None

@app.route('/contact')
def contact():
    return None