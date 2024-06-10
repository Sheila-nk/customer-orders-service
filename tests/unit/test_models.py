import pytest

from datetime import datetime

from customer_orders_service.models import User, Order


class TestUserModel:
    def test_new_user(self, new_user):
        """
        GIVEN a User model
        WHEN a new User is created
        THEN check id, username and registered_on are defined correctly
        """
        assert new_user.id == 'user_id'
        assert new_user.username == 'new_user'
        assert new_user.registered_on == datetime(2024, 6, 5, 20, 42, 30, 933213)
        assert isinstance(new_user.id, str)
        assert isinstance(new_user.username, str)
        assert isinstance(new_user.registered_on, datetime)


    def test_new_user_edge_cases(self):
        """
        GIVEN a User model
        WHEN a new User is created with edge cases
        THEN check id, username and registered_on are handled correctly
        """
        user = User(id='', username='', registered_on=None)
        assert user.id == ''
        assert user.username == ''
        assert user.registered_on is None
        assert isinstance(user.id, str)
        assert isinstance(user.username, str)
        

class TestOrderModel:    
    def test_new_order(self, new_order):
        """
        GIVEN an Order model
        WHEN a new Order is created
        THEN check order_id, item_name, num_of_items and phonenumber are defined correctly
        """
        assert new_order.item_name == 'shoes'
        assert new_order.num_of_items == 3
        assert new_order.phonenumber == '+254789123456'
        assert isinstance(new_order.item_name, str)
        assert isinstance(new_order.num_of_items, int)
        assert isinstance(new_order.phonenumber, str)


    def test_new_order_edge_cases(self):
        """
        GIVEN an Order model
        WHEN a new Order is created with edge cases
        THEN check item_name, num_of_items and phonenumber are handled correctly
        """
        order = Order(item_name='', num_of_items=0, phonenumber='')
        assert order.item_name == ''
        assert order.num_of_items == 0
        assert order.phonenumber == ''
        assert isinstance(order.item_name, str)
        assert isinstance(order.num_of_items, int)
        assert isinstance(order.phonenumber, str)


if __name__ == '__main__':
    pytest.main()