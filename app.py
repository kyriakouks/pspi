# BEGIN CODE HERE
from flask import Flask, url_for, render_template, request, redirect, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_cors import CORS
from pymongo import TEXT
# END CODE HERE

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/pspi"
CORS(app)
mongo = PyMongo(app)
mongo.db.products.create_index([("name", TEXT)])


if __name__ == "__main__":
    app.run(debug=True)  # only for our tests REMOVE LATER

@app.route("/search", methods=["GET"])
def search():
    # BEGIN CODE HERE
    print("tis  mamas  sou")
    query = request.args.get('query')
    print(query)
    if query:
        results = mongo.db.products.find({"$text": {"$search": query}})
        output = []
        for product in results:
            product['_id'] = str(product['_id'])  # Convert ObjectId to string
            output.append(product)
        return jsonify(output)
    else:
        return jsonify({"error": "No query provided"}), 400
    # END CODE HERE

@app.route("/add-product", methods=["POST"])
def add_product():
    # BEGIN CODE HERE
    collection = mongo.db.products
    data = request.json
    name = data.get('name')
    year = data.get('year')
    price = data.get('price')
    color = data.get('color')
    size = data.get('size')
    
    if not all([name, year, price, color, size]):
        return jsonify({"error": "Missing fields"}), 400
    
    product = {'name': name, 'year': year, 'price': price, 'color': color, 'size': size}
    collection.insert_one(product)
    
    return jsonify({"message": "Product added successfully"}), 201
    # END CODE HERE

@app.route("/content-based-filtering", methods=["POST"])
def content_based_filtering():
    # BEGIN CODE HERE
    data = request.json
    name = data.get('name')
    
    if not name:
        return jsonify({"error": "No product name provided"}), 400
    
    product = mongo.db.products.find_one({"name": name})
    
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    # Assuming a simple content-based filtering example by similar attributes
    similar_products = mongo.db.products.find({
        "color": product["color"],
        "size": product["size"],
        "price": {"$lte": product["price"] + 100, "$gte": product["price"] - 100}
    })
    
    output = []
    for sim_product in similar_products:
        sim_product['_id'] = str(sim_product['_id'])  # Convert ObjectId to string
        output.append(sim_product)
        
    return jsonify(output)
    # END CODE HERE

@app.route("/crawler", methods=["GET"])
def crawler():
    # BEGIN CODE HERE
    # Example crawler that retrieves and processes data
    # Since the specific details of the crawler are not provided, this will be a placeholder.
    
    def dummy_crawler():
        # Placeholder for actual web crawling logic
        # This should contain the logic to scrape data from web pages and store it in the database
        return [{"name": "Crawled Product 1"}, {"name": "Crawled Product 2"}]
    
    crawled_data = dummy_crawler()
    
    for item in crawled_data:
        mongo.db.products.insert_one(item)
    
    return jsonify({"message": "Crawling and insertion successful"}), 200
    # END CODE HERE
