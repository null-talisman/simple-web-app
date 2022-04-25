# simple web app
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    welcome_msg = """Welcome to SWA! \nPlease feel free to explore some of this app's functionality: \n"""
    return welcome_msg

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
        return "Your name is " + first_name + last_name
    return render_template("application.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)