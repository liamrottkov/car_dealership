from app import app, db
from datetime import datetime

# class Address(db.model):
#     address_id = db.Column(db.Integer, primary_key=True)
#     street_number = db.Column(db.Integer)
#     street_name = db.Column(db.String(100))
#     street2 = db.Column(db.String(100))
#     city = db.Column(db.String(100))
#     state = db.Column(db.String(20))
#     zipcode = db.Column(db.Integer)

class Car(db.Model):
    car_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    color = db.Column(db.String(100))

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    address_id = db.Column(db.Integer, db.ForeignKey('address.address_id'))
    date_created = db.Column(db.DateTime, default=datetime.now().date())
    phone_num = db.Column(db.Integer)

    # cars = db.relationship('Maintenance', backref=db.backref('customer', lazy='joined'))

# class Customer_Car(db.model):
#     cc_id = db.Column(db.Integer, primary_key=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
#     vin = db.Column(db.Integer, db.ForeignKey('vin.vin'))


class Maintenance(db.Model):
    maintenance_id = db.Column(db.Integer, primary_key=True)
    vin = db.Column(db.Integer, db.ForeignKey('vin.vin'))
    work = db.Column(db.String(400))
    date_posted = db.Column(db.DateTime, default=datetime.now().date())


# class Contact(db.Model):
#     contact_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     email = db.Column(db.String(80))
#     message = db.Column(db.String(500))
#     date_posted = db.Column(db.DateTime, default=datetime.now().date())

class Inventory(db.Model):
    inventory_id = db.Column(db.Integer, primary_key=True)
    vin = db.Column(db.Integer, db.ForeignKey('vin.vin'))
    date_aquired = db.Column(db.DateTime, default=datetime.now().date())

class Vin(db.Model):
    vin = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.car_id'))


# add user loader, when you call login_user this is how it finds the correct user to login
# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))
