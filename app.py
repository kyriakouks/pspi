# BEGIN CODE HERE
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import TEXT
# END CODE HERE

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/pspi"
CORS(app)
mongo = PyMongo(app)
mongo.db.products.create_index([("name", TEXT)])


@app.route("/search", methods=["GET"])
def search():
    # BEGIN CODE HERE
    
    return "<p>hello</p>"
    # END CODE HERE


@app.route("/add-product", methods=["POST"])
def add_product():
    # BEGIN CODE HERE
    new_product = request.json
    exists = mongo.db.products.find_one({"name": new_product["name"]})
    if exists is None:
        mongo.db.products.insert_one(new_product)
        return "Addition made"
    else:
        mongo.db.products.update_many({"name": new_product["name"]}, {"$set": {"price": new_product["price"], "production_year": new_product["production_year"], "color": new_product["color"], "size": new_product["size"]}})
        return "Updated"
    # data = request.json
    # name = data.get('name')
    # production_year = data.get('production_year')
    # price = data.get('price')
    # color = data.get('color')
    # size = data.get('size')

    
    # # Validate input data
    # if not (name and isinstance(production_year, int) and isinstance(price, (int, float)) and isinstance(color, int) and isinstance(size, int)):
    #     return jsonify({"error": "Invalid or missing data"}), 400

    # # Create or update product
    # product = {
    #     "name": name,
    #     "production_year": production_year,
    #     "price": price,
    #     "color": color,
    #     "size": size
    # }

    # existing_product = mongo.db.products.find_one({"name": name})
    

    # if existing_product:
    #     mongo.db.products.update_one(
    #         {"_id": existing_product["_id"]},
    #         {"$set": product}
    #     )
    #     return jsonify({"message": "Product updated"}), 200
    # else:
    #     mongo.db.products.insert_one(product)
    #     return jsonify({"message": "Product added"}), 201
    # END CODE HERE


@app.route("/content-based-filtering", methods=["POST"])
def content_based_filtering():
    # BEGIN CODE HERE
    return ""
    # END CODE HERE


@app.route("/crawler", methods=["GET"])
def crawler():
    # BEGIN CODE HERE
    return ""
    # END CODE HERE

if __name__ == '__main__':
    app.run(debug=True)