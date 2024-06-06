# BEGIN CODE HERE
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import TEXT
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# END CODE HERE

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/pspi"
CORS(app)
mongo = PyMongo(app)
mongo.db.products.create_index([("name", TEXT)])

@app.route("/search", methods=["GET"])
def search():
    # # BEGIN CODE HERE
    name = request.args.get('name') 
    results = list(mongo.db.products.find({'name': {'$regex': name, '$options': 'i'}}).sort('price',-1))

    found_products = []

    for r in results:
        product_schema = {
            "id": str(r['_id']),
            "name": r['name'],
            "production_year": r['production_year'],
            "price": r['price'],
            "color": r['color'],
            "size": r['size']
        }
        found_products.append(product_schema)


    return jsonify(found_products)
    # # END CODE HERE


@app.route("/add-product", methods=["POST"])
def add_product():
    # # BEGIN CODE HERE
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
    # # END CODE HERE
    


@app.route("/content-based-filtering", methods=["POST"])
def content_based_filtering():
    # BEGIN CODE HERE
    given_product = request.json
    given_product_metrics = [given_product['production_year'],given_product['price'],given_product['color'],given_product['size']]
    
    avaliable_products = list(mongo.db.products.find())

    similar = []
    for product in avaliable_products:
        metrics= [product['production_year'],product['price'],product['color'],product['size']]
        cosine_similarity = np.dot(given_product_metrics,metrics)/(np.linalg.norm(given_product_metrics)*np.linalg.norm(metrics))
        
        if cosine_similarity > 0.7:
          similar.append(product['name'])

    return jsonify(similar)
    # END CODE HERE


@app.route("/crawler", methods=["GET"])
def crawler():
    # BEGIN CODE HERE
    semester_number = request.args.get('semester')
    url = "https://qa.auth.gr/el/x/studyguide/600000438/current"

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    semester_table = driver.find_element(By.ID,'exam'+semester_number)
    semester_courses = list(semester_table.find_elements(By.TAG_NAME,'a'))
    courses = []
    for course in semester_courses:
        courses.append(course.text)

    return jsonify(courses)
    # END CODE HERE

if __name__ == "__main__":
    app.run(debug=True)  # only for our tests REMOVE LATER

