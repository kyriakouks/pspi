# BEGIN CODE HERE
from flask import Flask, url_for, render_template, request, redirect, jsonify # type: ignore
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_cors import CORS
from pymongo import TEXT
from bson import json_util
import json

# END CODE HERE

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/pspi"
CORS(app)
mongo = PyMongo(app)
mongo.db.products.create_index([("name", TEXT)])

def parse_json(data):
    return json.loads(json_util.dumps(data))


@app.route("/search", methods=["GET"])
def search():
    # # BEGIN CODE HERE
    try:
        name = request.args.get('name')
        inserted_name = mongo.db.products.find({"name": name})
        results = list(inserted_name) 
        parsed_results = parse_json(results)
        return jsonify({"results": parsed_results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    # # END CODE HERE


@app.route("/add-product", methods=["POST"])
def add_product():
    data = request.json
    query = {"name": data["name"]}
    exists = mongo.db.products.find_one(query)
    if exists:
        filter = {"name":data["name"]}
        update = {"$set": {"price": data["price"],"production_year":data["production_year"],"color":data["color"],"size":data["size"]}} 
        mongo.db.products.update_many(filter,update)
        return "updated item"
    else:
        mongo.db.products.insert_one(data)
        return "added item"


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

if __name__ == "__main__":
    app.run(debug=True)  # only for our tests REMOVE LATER

