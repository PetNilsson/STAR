"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/registertime', methods=['GET', 'POST'])
def registertime():
    if request.method == "GET" :
        return render_template(
            'registertime.html',
            title='Register time',
            year=datetime.now().year
        )
    time = request.form['worktime']
    customer = request.form['customer']
    return render_template(
        'timeregistered.html',
        worktime=time,
        customer=customer
    )
