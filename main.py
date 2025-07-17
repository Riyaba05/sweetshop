from flask import Flask, render_template, request, redirect, url_for
from src.sweet import Sweet
from src.sweetshop import SweetShop

app = Flask(__name__)
shop = SweetShop()

@app.route('/')
def index():
    sweets = shop.get_all_sweets()
    return render_template('index.html', sweets=sweets)

@app.route('/add', methods=['POST'])
def add_sweet():
    id = int(request.form['id'])
    name = request.form['name']
    category = request.form['category']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])
    sweet = Sweet(id, name, category, price, quantity)
    shop.add_sweet(sweet)
    return redirect(url_for('index'))

@app.route('/delete/<int:sweet_id>', methods=['POST'])
def delete_sweet(sweet_id):
    shop.delete_sweet(sweet_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=8080)

