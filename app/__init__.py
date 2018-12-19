# Import dependencies
import logging
import os
from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from itsdangerous import URLSafeTimedSerializer

# Import config file
from . import config

basedir = os.path.abspath(os.path.dirname(__file__))
logger = logging.getLogger(__name__)

# Initialise application with object file configuration
app = Flask(__name__, template_folder="../templates", static_folder='../static', static_url_path='')


config_map = {
    'development': config.Development(),
    'testing': config.Testing(),
    'production': config.Production(),
}
app.config.from_object(config_map['development'.lower()])
app.url_map.strict_slashes = False

# Enable CSRF protection
csrf = CSRFProtect(app)
# INnitialise Serializer
ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])
# Initialise database connection
db = SQLAlchemy(app)
db.init_app(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500


# Import a module / component using its blueprint handler variable (mod_auth)
from app.blog.controllers import mod_blog as blog_module
from app.home.controllers import mod_home as home_module

# Register blueprint(s)
app.register_blueprint(home_module)
app.register_blueprint(blog_module)



# db.configure_mappers()
# db.create_all()
# db.session.commit()