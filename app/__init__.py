from flask import Flask, render_template
# from flask_wtf.csrf import CSRFProtect
from config import Config
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma
from flask_cors import CORS
from helpers import JSONEncoder

app = Flask(__name__)

# csrf = CSRFProtect(app)
# app.config['SECRET_KEY'] = "secretkey"
# app.config['WTF_CSRF_SECRET_KEY'] = "secretkey"
# csrf.init_app(app)

CORS(app)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

app.json_encoder = JSONEncoder
app.config.from_object(Config)
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)