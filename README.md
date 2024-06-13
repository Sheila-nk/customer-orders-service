[![Tests](https://github.com/Sheila-nk/customer-orders-service/actions/workflows/test.yaml/badge.svg)](https://github.com/Sheila-nk/customer-orders-service/actions/workflows/test.yaml)


# Customer-Orders Service

The `Customer-Orders Service` is a Flask-based web application that handles user authentication and order management. 

The application is containerized using `Docker` and deployed on `Heroku`. It interacts with a `PostgreSQL` database for storing user and order information, authenticates users via [Google OAuth](https://developers.google.com/identity/protocols/oauth2), and uses the [Africa's Talking](https://africastalking.com/) API for sending SMS notifications.

## Table of Contents
1. [Architecture](#architecture)
1. [Setup](#setup)
2. [Running the Application](#running-the-application)
3. [API Endpoints](#api-endpoints)
    - [Authentication Endpoints](#authentication-endpoints)
    - [Order Management Endpoints](#order-management-endpoints)


### Architecture
![Service Architecure]('/images/architecture.png')

### Setup
To run the application locally using Docker, ensure you have the following installed:
- Python
- Docker

Clone the repository:
```sh
git clone https://github.com/Sheila-nk/customer-orders-service.git
cd customer-orders-service
```

Create a .env file:
```sh
touch .env
```
Add your environment variables in the `.env` file. It should include the following:

```
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=your_database_uri
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
AFRICASTALKING_USERNAME=your_africastalking_username
AFRICASTALKING_API_KEY=your_africastalking_api_key
```

Build and run the Docker container:
```sh
docker-compose up --build
```

### Running the Application

After setting up your environment and starting the Docker container, the application will be available at `http://localhost:8000`.

### API Endpoints
#### Authentication Endpoints
- `GET /auth/login`: Redirects the user to Google OAuth login.

    **Response**: Redirect to Google login page.

- `GET /auth/authorize`: Handles the Google OAuth callback and logs the user in.

    **Response**: JSON message indicating login success or error.

- `GET /logout`: Logs the user out.

    **Response**: JSON message indicating logout success.

#### Order Management Endpoints
- `POST /add_order`: Add a new order.

    **Request Body**:  
    ```json
    {
    "item_name": "Product Name",
    "num_of_items": 1,
    "phonenumber": "+254456789012"
    }
    ```
    **Response**: JSON message indicating order addition success or error.

- `PUT /update_order/<order_id>`: Update an existing order.

    **Request Body**:

    ```json
    {
    "item_name": "Updated Product Name",
    "num_of_items": 2
    }
    ```
    **Response**: JSON message indicating order update success or error.

- `DELETE /delete_order/<order_id>`: Delete an existing order.

    **Response**: JSON message indicating order deletion success or error.

