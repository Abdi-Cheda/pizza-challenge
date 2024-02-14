# Pizza Restaurant API
## Introduction
This is a simple Flask-based API for managing pizza restaurants and their menus. It allows users to perform CRUD operations on restaurants and pizzas, as well as associating pizzas with specific restaurants along with pricing information.

## Installation
Clone the repository:
git clone https://github.com/Abdi-Cheda/pizza-challenge.git

## Install dependencies:
pip install -r requirements.txt

## Set up the database:
flask db init
flask db migrate
flask db upgrade

Start the Flask server:

bash
Copy code
python app.py
Access the API endpoints using a tool like Postman or any web browser:

GET /restaurants: Retrieve all restaurants.
GET /restaurants/<id>: Retrieve a specific restaurant by ID.
DELETE /restaurants/<id>: Delete a restaurant by ID.
GET /pizzas: Retrieve all pizzas.
POST /restaurant_pizzas: Add a new pizza to a restaurant's menu along with pricing information.
Sample Data
You can add sample data to the database by running the add_sample_data function in the app.py file. Make sure to uncomment the call to this function at the end of the file.

Author
This project was developed by [Your Name].

License
This project is licensed under the MIT License.