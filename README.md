# Store Management API
Online Store Inventory and Supplier Management API

## Overview
This project implements an API for managing inventory items and suppliers for an online store. The API is built using Django REST Framework and allows for CRUD operations on items and suppliers, as well as establishing relationships between them.

## Prerequisites
- Python 3.8+
- Django 3.2+
- Django REST Framework

## Setup

### Clone the Repository
```bash
git clone https://github.com/IbroDante/online_store_API.git
cd online_store_API


Create a virtual environment
python -m venv env
source env/bin/activate  
# For Windows users: env\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Database Setup
python manage.py migrate

Run the Server
python manage.py runserver
The server runs at http://127.0.0.1:8000/api/

Testing
python manage.py test

API Endpoints / Usage

Items
GET /api/items/ : Retrieve a list of all items.
POST /api/items/ : Create a new item.
GET /api/items/{id}/ : Retrieve details of a specific item.
PUT /api/items/{id}/ : Update details of a specific item.
DELETE /api/items/{id}/ : Delete a specific item.

Suppliers
GET /api/suppliers/ : Retrieve a list of all suppliers.
POST /api/suppliers/ : Create a new supplier.
GET /api/suppliers/{id}/ : Retrieve details of a specific supplier.
PUT /api/suppliers/{id}/ : Update details of a specific supplier.
DELETE /api/suppliers/{id}/ : Delete a specific supplier.

Example Requests and Responses
Inventory Items
List all items
Endpoint: /api/items/
Method: GET
Response:

[
    {
        "id": 1,
        "name": "Item name",
        "description": "Description of item",
        "price": "29.34",
        "date_added": "2024-06-11T12:34:56.789012Z",
        "suppliers": [
            {
                "id": 1,
                "name": "Supplier name",
                "contact_information": "supplier contact"
            }
        ]
    }
]
Create a new item
Endpoint: /api/items/
Method: POST
Request Body:

{
    "name": "Item name",
    "description": "Description of item",
    "price": "23.99",
    "suppliers": [1, 2]
}
Response:

{
    "id": 2,
    "name": "Item name",
    "description": "Description of item",
    "price": "23.99",
    "date_added": "2024-06-12T12:34:56.789012Z",
    "suppliers": [
        {
            "id": 1,
            "name": "Supplier name",
            "contact_information": "contact"
        }
    ]
}
Retrieve an item
Endpoint: /api/items/{id}/
Method: GET
Response:

{
    "id": 1,
    "name": "Item name",
    "description": "Description of item",
    "price": "19.99",
    "date_added": "2024-06-11T12:34:56.789012Z",
    "suppliers": [
        {
            "id": 1,
            "name": "Supplier name",
            "contact_information": "contact"
        }
    ]
}
Update an item
Endpoint: /api/items/{id}/
Method: PUT
Request Body:

{
    "name": "Updated Item name",
    "description": "Updated Description of item",
    "price": "45.99",
    "suppliers": [1]
}
Response:

{
    "id": 1,
    "name": "Updated Item name",
    "description": "Updated Description of item",
    "price": "45.99",
    "date_added": "2024-06-11T12:34:56.789012Z",
    "suppliers": [
        {
            "id": 1,
            "name": "Supplier name",
            "contact_information": "contact"
        }
    ]
}
Delete an item
Endpoint: /api/items/{id}/
Method: DELETE
Response: 204 No Content

Suppliers
List all suppliers
Endpoint: /api/suppliers/
Method: GET
Response:


[
    {
        "id": 1,
        "name": "Supplier name",
        "contact_information": "supplier contact",
        "items": [
            {
                "id": 1,
                "name": "Item name",
                "description": "Description of item",
                "price": "29.34",
                "date_added": "2024-06-11T12:34:56.789012Z"
            }
        ]
    }
]
Create a new supplier
Endpoint: /api/suppliers/
Method: POST
Request Body:

{
    "name": "Supplier name",
    "contact_information": "supplier contact",
    "items": [1, 2]
}
Response:

{
    "id": 2,
    "name": "Supplier name",
    "contact_information": "supplier contact",
    "items": [
        {
            "id": 1,
            "name": "Item name",
            "description": "Description of item",
            "price": "29.34",
            "date_added": "2024-06-11T12:34:56.789012Z"
        }
    ]
}
Retrieve a supplier
Endpoint: /api/suppliers/{id}/
Method: GET
Response:

{
    "id": 1,
    "name": "Supplier name",
    "contact_information": "supplier contact",
    "items": [
        {
            "id": 1,
            "name": "Item name",
            "description": "Description of item",
            "price": "29.34",
            "date_added": "2024-06-11T12:34:56.789012Z"
        }
    ]
}
Update a supplier
Endpoint: /api/suppliers/{id}/
Method: PUT
Request Body:

{
    "name": "Updated Supplier name",
    "contact_information": "updated supplier contact",
    "items": [1]
}
Response:

{
    "id": 1,
    "name": "Updated Supplier name",
    "contact_information": "updated supplier contact",
    "items": [
        {
            "id": 1,
            "name": "Item name",
            "description": "Description of item",
            "price": "29.34",
            "date_added": "2024-06-11T12:34:56.789012Z"
        }
    ]
}
Delete a supplier
Endpoint: /api/suppliers/{id}/
Method: DELETE
Response: 204 No Content

### Notes:
- Make sure to replace placeholders `{id}` with actual IDs when making request.