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
    if request.method == "POST":
        return render_template("about.html")
    return render_template("about.html")

@app.route("/products")
def products():
    if request.method == "POST":
        return render_template("products.html")
    return render_template("products.html")

@app.route("/careers")
def careers():
    if request.method == "POST":
        return render_template("careers.html")
    return render_template("careers.html")

@app.route("/contact")
def contact():
    if request.method == "POST":
        return render_template("contact.html")
    return render_template("contact.html")

@app.route("/apply")
def apply():
    if request.method == "POST":
        # getting input with references in HTML form
        first_name = request.form.get("fname")
        middle_initial = request.form.get("mname")
        last_name = request.form.get("lname")
        birth_date = request.form.get("birthdate")
        phone_number = request.form.get("phonenumber")
        email_address = request.form.get("emailaddress")
        college = request.form.get("place")
        degree = request.form.get("degree")
        major = request.form.get("major")
        minor = request.form.get("minor")
        graddate = request.form.get("graddate")
        return "Your name is " + first_name + last_name
    return render_template("application.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
