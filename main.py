from flask import Flask, render_template, request
from src.sweetshop import SweetShop

app = Flask(__name__)
shop = SweetShop()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        category = request.form.get("category")
        price = float(request.form.get("price"))
        quantity = int(request.form.get("quantity"))
        shop.add_sweet(name, category, price, quantity)
    return render_template("index.html", sweets=shop.get_all_sweets())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


