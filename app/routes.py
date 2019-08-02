from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import MaintenanceForm
from app.models import Maintenance, Inventory, Car
from flask_login import current_user

@app.route('/')
@app.route('/index')
@app.route('/index/<header>', methods=['GET'])
def index(header=''):
    products = [
        {
            'id': 1001,
            'title': 'Ford',
            'url': '../static/images/ford.jpg'
        },
        {
            'id': 1002,
            'title': 'Honda',
            'url': '../static/images/honda.jpg'
        },
        {
            'id': 1003,
            'title': 'Nissan',
            'url': '../static/images/nissan.jpg'
        },
    ]

    return render_template('index.html', products=products, title='Home', header=header)



@app.route('/inventory')
def inventory():

    cars = Inventory.query.all().join(Car)

    return render_template('inventory.html', cars=cars, title='Inventory')



@app.route('/maintenance')
def maintenance():
    form = MaintenanceForm()

    if form.validate_on_submit():

        maintenance = Maintenance(
            vin = form.vin.data,
            work = form.work.data
        )

        db.session.add(maintenance)
        db.session.commit()

        flash("Logged record.")

        return redirect(url_for('maintenance'))


    return render_template('form.html', form=form, title='Maintenance')
