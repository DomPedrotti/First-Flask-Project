from flask import render_template
from app import app

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
    return render_template('index.html', posts = posts)
