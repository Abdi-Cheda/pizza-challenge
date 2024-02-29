from models import db
from app import app
from models import Restaurant, Pizza, RestaurantPizza

def add_sample_data():
    with app.app_context():
        print("Deleting existing data...")
        db.session.query(RestaurantPizza).delete()
        db.session.query(Pizza).delete()
        db.session.query(Restaurant).delete()
        db.session.commit()

        print("Adding sample restaurants...")
        restaurant1 = Restaurant(name="Italiano's Pizza", address="123 Pizza Street")
        restaurant2 = Restaurant(name="New York Pizza Kitchen", address="456 Pie Avenue")
        db.session.add(restaurant1)
        db.session.add(restaurant2)

        print("Adding sample pizzas...")
        pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
        pizza2 = Pizza(name="Pepperoni", ingredients="Pepperoni, Tomato, Mozzarella")
        db.session.add(pizza1)
        db.session.add(pizza2)

        db.session.commit()

        print("Creating restaurant-pizza associations...")
        rp1 = RestaurantPizza(restaurant_id=restaurant1.id, pizza_id=pizza1.id, price=10.99)
        rp2 = RestaurantPizza(restaurant_id=restaurant1.id, pizza_id=pizza2.id, price=12.99)
        rp3 = RestaurantPizza(restaurant_id=restaurant2.id, pizza_id=pizza1.id, price=11.49)
        rp4 = RestaurantPizza(restaurant_id=restaurant2.id, pizza_id=pizza2.id, price=13.49)

        db.session.add(rp1)
        db.session.add(rp2)
        db.session.add(rp3)
        db.session.add(rp4)
        db.session.commit()

        print("Sample data added successfully!")

if __name__ == "__main__":
    add_sample_data()
