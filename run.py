import os
from customer_orders_service import create_app


if __name__ == "__main__":
    app = create_app()
    port = os.environ.get('PORT', 8000)
    app.run(debug=False, port=port)