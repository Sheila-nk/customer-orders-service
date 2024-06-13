#!/bin/bash

flask db upgrade head

gunicorn -w 2 -b 0.0.0.0:$PORT 'customer_orders_service:create_app()'