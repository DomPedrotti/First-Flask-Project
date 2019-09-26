from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for user {}, rmemeber_me {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

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

