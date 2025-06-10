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


if __name__ == "__main__":
    app.run(port=8000, debug=True)
