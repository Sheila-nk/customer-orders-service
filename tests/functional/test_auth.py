import json
import pytest

from unittest.mock import patch
from flask import session


class TestAuthBluePrint:

    def test_login(self, test_client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/auth/login' endpoint is requested (GET)
        THEN check that the response is a redirect to Google Oauth
        """
        response = test_client.get('/auth/login')
        assert response.status_code == 302

        assert response.headers['Location'].startswith('https://accounts.google.com/o/oauth2/v2/auth')


    @patch('customer_orders_service.oauth.google.authorize_access_token')
    def test_authorize(self, mock_authorize_access_token, test_client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/auth/authorize' endpoint is requested (GET)
        THEN check that the response indicates successful login and the user session is set
        """
        # mock the response from the OAuth authorization
        mock_access_token = {
            'userinfo': {
                'sub': '1234abc',
                'name': 'test_user'
            }
        }
        mock_authorize_access_token.return_value = mock_access_token

        response = test_client.get('/auth/authorize')
        assert response.status_code == 200

        response_data = json.loads(response.data.decode('utf-8'))
        assert response_data['message'] == 'Login successful. Welcome test_user'
        assert session['user'] == '1234abc'


    def test_logout(self, test_client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/auth/logout' endpoint is requested (GET)
        THEN check that the response indicates successful logout and the user session is cleared
        """
        # define user within session transaction
        with test_client.session_transaction() as session:
            session['user'] = '1234abc'

        response = test_client.get('/auth/logout')
        assert response.status_code == 200

        response_data = json.loads(response.data.decode('utf-8'))
        assert response_data['message'] == 'Logout successful. Goodbye!'
        
        # start a new session transaction to verify session state
        with test_client.session_transaction() as session:
            assert 'user' not in session


if __name__ == '__main__':
    pytest.main()