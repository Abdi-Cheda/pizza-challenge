from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route("/")
def home():
           return "Hello World!!!"
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address
    } for restaurant in restaurants])

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        return jsonify({
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'pizzas': [{
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            } for pizza in restaurant.pizzas]
        })
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    } for pizza in pizzas])

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if not (price and pizza_id and restaurant_id):
        return jsonify({'errors': ['Missing required fields']}), 400

    if not (1 <= price <= 30):
        return jsonify({'errors': ['Price must be between 1 and 30']}), 400

    restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(restaurant_pizza)
    db.session.commit()

    pizza = Pizza.query.get(pizza_id)
    if pizza:
        return jsonify({
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }), 201
    else:
        return jsonify({'error': 'Pizza not found'}), 404

if __name__ == '__main__':
    app.run(port=5555)