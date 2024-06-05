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

    from .models import User, Order

    migrate.init_app(app, db)

    from .auth.views import auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app