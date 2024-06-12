import africastalking

from authlib.integrations.flask_client import OAuth
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from .config import ApplicationConfig


convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
oauth = OAuth()
migrate = Migrate(db, render_as_batch=True)

def create_app(config=ApplicationConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    oauth.init_app(app)

    with app.app_context():
        oauth.register(
            name= 'google',
            client_id=app.config['GOOGLE_CLIENT_ID'],
            client_secret=app.config['GOOGLE_CLIENT_SECRET'],
            server_metadata_url=app.config['GOOGLE_DISCOVERY_URL'],
            client_kwargs={
                'scope': 'openid email profile'
            }
        )

        username = app.config['AT_USERNAME']
        api_key = app.config['AT_API_KEY']

    africastalking.initialize(username, api_key)

    from .models import User, Order

    migrate.init_app(app, db)

    from .auth.views import auth_blueprint
    from .orders.views import orders_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(orders_blueprint, url_prefix='/orders')

    @app.after_request
    def set_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['Content-Security-Policy'] = "frame-ancestors 'self'"
        response.headers['Strict-Transport-Security'] = 'max-age=31536000;'
        return response

    return app