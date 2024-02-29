from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    pizzas = db.relationship('Pizza', secondary='restaurant_pizzas', backref='restaurants')

class Pizza(db.Model):
    __tablename__ = 'pizza'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    pizza_restaurants = db.relationship('Restaurant', secondary='restaurant_pizzas', back_populates='pizzas')

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)

    @classmethod
    def validate_price(cls, price):
        return 1 <= price <= 30