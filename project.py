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
@app.route('/restaurant/new/')
def newRestaurant():
    return 'Novo restaurante'

# Edit a Restaurant
@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    return 'Edita o restaurante'

# Delete a Restaurant
@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    return 'Delete um restaurante'

# Show a restaurant menu
@app.route('/restaurant/<int:restaurant_id>/', methods=['GET', 'POST'])
@app.route('/restaurant/<int:restaurant_id>/menu/', methods=['GET', 'POST'])
def showMenu(restaurant_id):
    return 'Mostra os itens de menu do restaurante'

# Create a new menu item
@app.route('/restaurant/<int:restaurant_id>/menu/item/')
def newMenuItem(restaurant_id):
    return 'NOVO ITEM DO MENU'

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
