# simple web app
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/home")
def home():
    if request.method == "POST":
        return render_template("home.html")
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/careers")
def careers():
    return render_template("careers.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/apply")
def apply():
    """
    TODO: Store application info as an "Application"
    TODO: Store the application in a DB or simply send an email with it
    """
    return render_template("application.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
