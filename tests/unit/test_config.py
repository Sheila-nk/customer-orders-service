import pytest

class TestAppConfig:

    def test_config(self, test_client):
        """
        GIVEN a Flask application configured for testing
        WHEN the configuration is loaded
        THEN the TESTING flag, SECRET_KEY and SQLALCHEMY_DATABASE_URI should be set correctly
        """
        app = test_client.application
        assert app.config['TESTING'] is True
        assert app.config['SECRET_KEY'] == 'testing'
        assert app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://localhost/test_db'

    
if __name__ == "__main__":
    pytest.main()