from flask import render_template
from app import app

# @app.route is a "decorator", which is python's way of modifying the following function
# when the user runs either / or /index URL, the following index function is called
@app.route('/')
@app.route('/index')
def index():
    # set dummy object before we make things dynamic
    user = {'username': 'Miguel'}
    # returns a function that renders the index template instead of defining it all here
    posts = [
        # example posts
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)