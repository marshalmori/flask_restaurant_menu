from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

# DB Configs
engine = create_engine('sqlite:///restaurant.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Show all restaurants
@app.route('/')
@app.route('/restaurant/')
def showRestaurant():
    restaurant = session.query(Restaurant).all()
    return render_template('restaurant.html', restaurant=restaurant)


# Create a new Restaurant
@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        newRest = Restaurant(name=request.form['name'])
        session.add(newRest)
        session.commit()
        return redirect(url_for('showRestaurant'))
    else:
        return render_template('newRestaurant.html')

# Edit a Restaurant
@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
        session.add(editedRestaurant)
        session.commit()
        return redirect(url_for('showRestaurant'))
    else:
        return render_template('editRestaurant.html', restaurant_id = restaurant_id, restaurant = editedRestaurant)


# Delete a Restaurant
@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    deletedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(deletedRestaurant)
        session.commit()
        return redirect(url_for('showRestaurant'))
    else:
        return render_template('deleteRestaurant.html', restaurant_id = restaurant_id, item = deletedRestaurant)

# Show a restaurant menu
@app.route('/restaurant/<int:restaurant_id>/', methods=['GET', 'POST'])
@app.route('/restaurant/<int:restaurant_id>/menu/', methods=['GET', 'POST'])
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return render_template('menu.html', restaurant=restaurant, items=items)

# Create a new menu item
@app.route('/restaurant/<int:restaurant_id>/menu/item/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'],
                           description=request.form['description'],
                           price=request.form['price'],
                           course=request.form['course'],
                           restaurant_id = restaurant_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('showMenu', restaurant_id = restaurant_id))
    else:
        return render_template('newMenu.html', restaurant_id = restaurant_id )

# Edit menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return 'Editar Item de Menu'

# Deletar item do menu
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return 'DELETAR'



if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
