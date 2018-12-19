# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import database model for queries and search
from app.blog.models import Post

# Import app and database session
from app import db, app

# Import database functions
from sqlalchemy import desc
from sqlalchemy import and_

# Define the blueprint
mod_blog = Blueprint('blog', __name__, url_prefix='/blog')


@mod_blog.route('/')
@mod_blog.route('/index')
def index():
   '''
      Display all published posts.
   '''
   # Try to get all, recent and most popular posts.
   try:
       posts = Post.query.filter(and_(Post.published == True, Post.suspended == False)).all()
   except:
       posts = []
   return render_template('index.html', posts=posts)


@mod_blog.route('/about')
def about():
    return render_template('blog/about.html')


@mod_blog.route('/<string:slug>')
def post(slug):
    '''
       Display a given post using its slug
    '''
    # Try to get the given post
    try:
        post = Post.query.filter_by(slug=slug).first()
    except:
        post = None

    # increment the views of the post
    try:
       post.views = post.views + 1
       db.session.commit()
    except:
       pass
    return render_template('blog/post.html', post=post)

