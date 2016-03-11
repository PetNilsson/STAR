# -*- coding: utf-8 -*-
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for
from FlaskWebProject import app
from FlaskWebProject.models import Report, User
from flask.ext.login import LoginManager, login_required

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
    workDay = request.form['workday']
    customer = request.form['customer']
    report = Report(
            workDate=workDay,
            worker="Peter",
            time=time
    )
    report.save()
    return render_template(
            'timeregistered.html',
            worktime=time,
            customer=customer
    )


@app.route('/edituser', methods=['GET', 'POST', 'DELETE'])
def edituser():
    if request.method == "GET" :
        if request.args.get("id"):
            user = User.objects.get(id=request.args.get("id"))
            return render_template(
                'edituser.html',
                legend=u"Redigera användare",
                user=user
            )
        return render_template(
                'edituser.html',
                legend=u"Lägg till ny användare",
            user=User()
        )
    if request.method == "POST" :
        if request.args.get('action') == 'delete':
            user = User.objects.get(id=request.args.get("id"))
            if user :
                user.delete()
                return redirect(url_for('users'))
            return "Not found", 404
        else:
            if request.args.get("id"):
                User.objects(id=request.args.get("id")).update_one(
                    set__username=request.form['username'],
                    set__password=request.form['password'],
                    set__firstname=request.form['firstname'],
                    set__lastname=request.form['lastname'],
                    set__email=request.form['email'],
                    upsert=True
                )
            else:
                user=User()
                user.username=request.form['username']
                user.password=request.form['password']
                user.firstname=request.form['firstname']
                user.lastname=request.form['lastname']
                user.email=request.form['email']
                user.save()
            return redirect(url_for('users'))

@app.route('/users', methods=['GET'])
def users():
    users = User.objects.all()
    return render_template(
        'userlist.html',
        users=users
    )

@app.route('/machines', methods=['GET'])
@login_required
def machines():
    return 'Maskiner'