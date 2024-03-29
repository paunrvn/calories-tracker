# Import all the flask related functions
from flask import Flask, render_template, request
# Import the database object which is initialized in the models module
from models import db, Food
from datetime import date

# Initialize a Flask object on which we can write routes
app = Flask(__name__)

# We configure the SQLALCHEMY Database location
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///calories.db"

# We initialize the database connection
db.init_app(app)


@app.route("/")
def home():
    day = request.args.get('day')

    # The first request should show the data for today
    if not day:
        day = date.today()

    breakfast_food = Food.query.filter_by(date=day, meal='breakfast').all()
    lunch_food = Food.query.filter_by(date=day, meal='lunch').all()
    dinner_food = Food.query.filter_by(date=day, meal='dinner').all()

    return render_template("hello.html",
                           breakfast_food=breakfast_food,
                           lunch_food=lunch_food,
                           dinner_food=dinner_food,
                           day=day)
