import os
import pytest
from datetime import datetime

from customer_orders_service import create_app
from customer_orders_service.config import TestingConfig
from customer_orders_service.models import User, Order


@pytest.fixture(scope='module')
def test_client():
    """
    This fixture creates a Flask test client using the TestingConfig configuration.
    The fixture will be set up once per module, and the same client will be used across 
    all tests in the module.
    """
    app = create_app(config=TestingConfig)
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


@pytest.fixture(scope='module')
def new_user():
    # Fixture for creating a new user
    return User(id='user_id', username='new_user', registered_on=datetime(2024, 6, 5, 20, 42, 30, 933213))


@pytest.fixture(scope='module')
def new_order():
    # Fixture for creating a new order
    return Order(item_name='shoes', num_of_items=3, phonenumber='+254789123456')