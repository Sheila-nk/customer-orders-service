from flask import Blueprint, jsonify, session, url_for
from flask.views import MethodView
from customer_orders_service import db, oauth
from customer_orders_service.models import User


auth_blueprint = Blueprint('auth', __name__)


class LoginAPI(MethodView):
    def get(self):
        redirect_uri = url_for('auth.authorize_api', _external=True)
        return oauth.google.authorize_redirect(redirect_uri)
    
login_view = LoginAPI.as_view('login_api')
auth_blueprint.add_url_rule(
    '/login',
    view_func=login_view,
    methods=['GET']
)
    
    
class AuthorizeAPI(MethodView):
    def get(self):
        token = oauth.google.authorize_access_token()
        user_info = token['userinfo']
        if user_info:
            try:
                user = User.query.filter_by(id=user_info['sub']).first()
                if not user:
                    user = User(
                        id=user_info['sub'],
                        username=user_info['name']
                    )
                    db.session.add(user)
                    db.session.commit()
                session['user'] = user.id
                return jsonify({'message': f'Login successful. Welcome {user.username}'}), 200

            except Exception as e:
                return jsonify({'message': f'Ooops! Something went wrong!: {e}'}), 500

    
authorize_view = AuthorizeAPI.as_view('authorize_api')
auth_blueprint.add_url_rule(
    '/authorize',
    view_func=authorize_view,
    methods=['GET']
)

class LogoutAPI(MethodView):
    def get(self):
        session.pop('user', None)
        return jsonify({'message': 'Logout successful. Goodbye!'}), 200

    
logout_view = LogoutAPI.as_view('logout_api')
auth_blueprint.add_url_rule(
    '/logout',
    view_func=logout_view,
    methods=['GET']
)