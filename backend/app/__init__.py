from flask import Flask
from flask_apscheduler import APScheduler
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from apis import api
from app.config import ProductionConfig
from app.db import db, reset_database

jwt = JWTManager()
scheduler = APScheduler()


def create_app():
    app = Flask(__name__)

    CORS(app,
         supports_credentials=True,
         resources={
             r'/api/*': {
                 'origins': '*',
                 'allow_headers': ['Content-Type', 'Authorization']
             }
         })
    app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
    app.config.from_object(ProductionConfig)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600
    scheduler.init_app(app)
    scheduler.start()

    register_api()

    from apis import api_blueprint
    app.register_blueprint(api_blueprint)

    app.url_map.strict_slashes = False
    jwt._set_error_handler_callbacks(api)
    return app


def register_api():
    from app.views.user_views import ns as user_views
    api.add_namespace(user_views)
