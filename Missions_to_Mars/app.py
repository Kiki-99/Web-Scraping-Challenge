from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)


#Get the main route and connection code between mongo and the app.py 
#def scrape(): #upsert #update (comes first) to retrieve information 
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update(
       {},
       mars_data,
       upsert=True
    )
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True),

