from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# ---------------- Utility Functions ----------------

def load_products():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_products(products):
    with open("products.json", "w") as file:
        json.dump(products, file, indent=4)

# ---------------- Routes ----------------

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Product API is running"})

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(load_products())

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    products = load_products()
    for p in products:
        if p["id"] == product_id:
            return jsonify(p)
    return jsonify({"error": "Product not found"}), 404

@app.route("/products", methods=["POST"])
def create_product():
    data = request.json

    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Invalid product data"}), 400

    products = load_products()

    new_product = {
        "id": max([p["id"] for p in products], default=0) + 1,
        "name": data["name"],
        "price": data["price"],
        "category": data.get("category", ""),
        "stock": data.get("stock", 0)
    }

    products.append(new_product)
    save_products(products)

    return jsonify(new_product), 201

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    products = load_products()
    for p in products:
        if p["id"] == product_id:
            p.update(request.json)
            save_products(products)
            return jsonify(p)
    return jsonify({"error": "Product not found"}), 404

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    products = load_products()
    new_products = [p for p in products if p["id"] != product_id]

    if len(products) == len(new_products):
        return jsonify({"error": "Product not found"}), 404

    save_products(new_products)
    return jsonify({"message": "Deleted successfully"}), 200

# ---------------- Run App (Railway Compatible) ----------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
