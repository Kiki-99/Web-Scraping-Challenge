from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/scrape_mars")


#Get the main route and connection code between mongo and the app.py 
#def scrape(): #upsert #update (comes first) to retrieve information 
@app.route("/")
def index():
    #Find Data
    mars_facts = mongo.db.collection.find_one()
    
    #Return template and data
    return render_template("index.html", mars= mars_facts)

#Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    #Run the scrape fuction
    mars_data = scrape_mars.scrape()
    
    #Update the Mongo Database using udate and upsert
    mongo.db.collection.update({}, mars_data, upsert=True)

    #Redirct back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True),

