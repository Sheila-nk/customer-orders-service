from flask import Blueprint, request, jsonify, session
from flask.views import MethodView

from customer_orders_service import db
from customer_orders_service.models import Order
from .validation import CreateAddOrderSchema, CreateUpdateOrderSchema


orders_blueprint = Blueprint('orders', __name__)

class AddOrderAPI(MethodView):
    def post(self):
        print('B: Session data: %s', session)
        post_data = request.get_json()
        add_order_schema = CreateAddOrderSchema()
        errors = add_order_schema.validate(post_data)
        if errors:
            return jsonify({'message': errors}), 400
        
        try:
            order = Order(**post_data)
            order.user_id = session['user']
            db.session.add(order)
            db.session.commit()
            return jsonify({"message": "Order added successfully!"}), 201
        
        except Exception as e:
            return jsonify({'message': f'Something went wrong: {e}'}), 500
    
add_order_view = AddOrderAPI.as_view('add_order_api')
orders_blueprint.add_url_rule(
    '/add_order',
    view_func=add_order_view,
    methods=['POST']
)


class UpdateOrderAPI(MethodView):
    def put(self, order_id):
        put_data = request.get_json()
        update_order_schema = CreateUpdateOrderSchema()
        errors = update_order_schema.validate(put_data)
        if errors:
            return jsonify({'message': errors}), 400
        
        order = Order.query.filter_by(order_id=order_id).first()
        if not order:
            return jsonify({'message': 'Order does not exist'}), 404
        
        try:
            for key, value in put_data.items():
                setattr(order, key, value)
            db.session.commit()
            return jsonify({"message": "Order updated successfully!"}), 200
        
        except Exception as e:
            return jsonify({'message': f'Ooops! Something went wrong: {e}'}), 500
    
update_order_view = UpdateOrderAPI.as_view('update_items_api')
orders_blueprint.add_url_rule(
    '/update_order/<order_id>',
    view_func=update_order_view,
    methods=['PUT']
)


class DeleteOrderAPI(MethodView):
    def delete(self, order_id):
        order = Order.query.filter_by(order_id=order_id).first()
        if not order:
            return jsonify({'message': 'Order does not exist'}), 404
        
        try:
            db.session.delete(order)
            db.session.commit()
            return jsonify({"message": "Order deleted successfully!"}), 200
        
        except Exception as e:
            return jsonify({'message': f'Ooops! Something went wrong: {e}'}), 500
    
delete_order_view = DeleteOrderAPI.as_view('delete_order_api')
orders_blueprint.add_url_rule(
    '/delete_order/<order_id>',
    view_func=delete_order_view,
    methods=['DELETE']
)
