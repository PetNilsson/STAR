from functools import wraps
from flask import request, Response, url_for, redirect, render_template
from flask.ext.login import login_user, logout_user, login_required
from flask.ext.wtf import Form
from FlaskWebProject.models import User
from FlaskWebProject import login_manager, app
from .forms import LoginForm

@login_manager.user_loader
def load_user(username):
    user = User.objects.get(username=username)
    if user :
        return user
    return None

@login_manager.request_loader
def load_user(request):
    token = request.headers.get('Authorization')
    if token is None:
        token = request.args.get('token')

    if token is not None:
        username,password = token.split(":")
        user_entry = User.get(username)
        if user_entry is not None:
            if user_entry.password == password:
                return user_entry
    return None

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm(csrf_enabled=False)
    if request.method=='POST' and form.validate_on_submit():
        user = User.objects.get(username=form.username.data)
        if user and User.validate_login(user.password, form.password.data):
            login_user(user)
            return redirect(request.args.get("next") or url_for("home"))
    return render_template('login.html', legend='Logga in', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

''''
def check_auth(username, password):
    user = User.objects.get(username=username)
    if user :
        if user.password == password:
            return True
    return False

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
    '''''