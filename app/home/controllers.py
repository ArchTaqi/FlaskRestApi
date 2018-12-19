# Import flask dependencies
from flask import Blueprint, request, render_template

# Define the blueprint
mod_home = Blueprint('home', __name__, url_prefix='/')


@mod_home.route('/')
@mod_home.route('/index')
def index():
    return render_template('index.html')

