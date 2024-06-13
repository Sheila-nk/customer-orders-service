import json
import pytest

from customer_orders_service import db
from customer_orders_service.models import User, Order



class TestOrderBlueprint:
    def test_add_order(self, test_client, db_user_and_order):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/orders/add_order' endpoint is requested (POST)
        THEN check that the response indicates successful addition of an order
        """
        user, order = db_user_and_order

        with test_client.session_transaction() as session:
            session['user'] = user.id

        order_data = {
            'item_name': 'Books',
            'num_of_items': 3,
            'phonenumber': '+254796749735'
        }

        response = test_client.post('/orders/add_order', json=order_data)
        assert response.status_code == 201

        response_data = json.loads(response.data.decode('utf-8'))
        assert response_data['message'] == 'Order added successfully but we were unable to send SMS!'


    def test_update_order(self, test_client, db_user_and_order):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/orders/update_order/<order_id>' endpoint is requested (PUT)
        THEN check that the response indicates successful update of an order
        """
        user, order = db_user_and_order

        update_data = {
            'item_name': 'Sweets',
            'num_of_items': 100
        }
        response = test_client.put(f'/orders/update_order/{order.order_id}', json=update_data)
        assert response.status_code == 200

        response_data = json.loads(response.data.decode('utf-8'))
        assert response_data['message'] == 'Order updated successfully!'


    def test_delete_order(self, test_client, db_user_and_order):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/orders/delete_order/<order_id>' endpoint is requested (DELETE)
        THEN check that the response indicates successful deletion of an order
        """
        user, order = db_user_and_order

        response = test_client.delete(f'/orders/delete_order/{order.order_id}')
        assert response.status_code == 200

        response_data = json.loads(response.data.decode('utf-8'))
        assert response_data['message'] == 'Order deleted successfully!'

        order_exists = Order.query.filter_by(order_id=order.order_id).first()
        assert order_exists is None
