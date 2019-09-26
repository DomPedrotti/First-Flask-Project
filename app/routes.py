from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username' : "Dom"}
    posts = [
        {
            'author': {'username': 'Dom'},
            'body' : 'Excited to start busting out this flask app'
        },
        {
            'author' : {'username': 'Everyone Else'},
            'body': 'Wow, Dom, this is so legit!' 

        }
    ]
    return render_template('index.html', user=user, posts = posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
