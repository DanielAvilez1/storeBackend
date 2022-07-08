from flask import Flask
from about import me
from data import mock_data
import json

app = Flask('server')


@app.get("/")
def home():
    return "Hello, world!"


@app.get("/test")
def test():
    return "this is just a simple test"


@app.get("/about")
def about_me():
    return "Daniel Avilez"


################################################################
########### API ENDPOINTS = PRODUCTS ###########################
################################################################

@app.get("/api/version")
def version():
    return "1.0"


@app.get("/api/about")
def about_json():
    return json.dumps(me)


@app.get("/api/products")
def get_products():
    return json.dumps(mock_data)


@app.get("/api/products/<id>")
def get_products_by_id(id):
    for prod in mock_data:
        if str(prod["id"]) == id:  # added str because id is a number
            return json.dumps(prod)

    return "NOT FOUND !"


@app.get("/api/products_category/<category>")
def get_prods_category(category):
    results = []
    category = category.lower()
    for prod in mock_data:
        if prod["category"] .lower() == category:
            results.append(prod)

    return json.dumps(results)


@app.get("/api/product_cheapest")
def get_cheapest():
    solution = mock_data[0]
    for prod in mock_data:
        if prod["price"] < solution["price"]:
            solution = prod

    return json.dumps(solution)


@app.get("/api/categories")
def get_categories():
    categories = []
    for product in mock_data:
        cat = product["category"]
        if not cat in categories:
            categories.append(cat)

    return json.dumps(categories)


# get/api/catagories
# return the list of categories
# 1 return ok
# 2 travel mock_data, and print the category of every product
# 3 put the category in a list and at the end of the for loop, return the list as json
app.run(debug=True)
