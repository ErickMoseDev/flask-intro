from flask import Flask, request


# the heart of the application
app = Flask(__name__)


# routes
@app.route("/")
def home():
    return "<h1>Happy Home route demo</h1>"


@app.route("/users", methods=["GET", "POST", "PATCH", "DELETE"])
def get_users():
    if request.method == "POST":
        return {"message": "This is the post method"}
    return {"message": "This will return all users"}


# syntatic sugar/ shortcuts for the common http verbs


@app.get("/products")
def get_all_products():
    pass


@app.post("/products")
def create_product():
    pass


@app.patch("/products/<int:id>")
def update_product(id):
    return f"Product {id} updated"


@app.delete("/products/<int:id>")
def delete_product(id):
    return f"Product {id} deleted"


# flask-restful - later
# work with classes and OOP techniques
# running flask apps

# resource naming conventions
# api documentation techniques
# swagger
# postman collections
# test api endpoints on postman / thunder client
# flask-sqlalchemy


# ecommerce endpoints
# @app.routes("/customers", methods=["POST"])
@app.post("/customers")
def add_customer():
    pass


# @app.routes("/customers")
@app.get("/customers")
def get_all_customers():
    pass


# fetch a single customer
# @app.routes("/customers/<int:id>", methods=["GET"])
@app.get("/customers/<int:id>")
def get_one_customer(id):
    pass


# @app.routes("/customers/<int:id>", methods=["PATCH"])
@app.patch("/customers/<int:id>")
def update_customer(id):
    pass


# @app.routes("/customers/<int:id>", methods=["DELETE"])
@app.delete("/customers/<int:id>")
def delete_customer(id):
    pass


""" 
create product - "/products" - [post]
all products - "/products" - [get]
one product  - "/products/<id>" [get]
update one product  - "/products/<id>" - [patch]
delete one product  - "/products/<id>" - [delete]

this-is-kebab-case

https://restfulapi.net/resource-naming/

"/customers"
"/customers/<id>"


"/customers/<id>/orders"
"/orders"
"/orders/<id>"
"/products"
"/products/<id>"

https://moringa.instructure.com/courses/1028/assignments/73067?module_item_id=171913

# api versioning

/api/v1/customers
/api/v1/customers/<id>
/api/v1/products
/api/v1/products/<id>

# breaking changes

/api/v2/customers
/api/v2/customers/<id>
/api/v2/products
/api/v2/products/<id>

# query parameters 
"/customers?api_version=1"

"""

if __name__ == "__main__":
    app.run(port=8000, debug=True)
