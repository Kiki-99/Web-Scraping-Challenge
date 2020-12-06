from flask import Flask,render_template,redirect
from flask_pymongo 
import PyMongo 
import scrape_mars


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.current_mars_info
collection = db.mars_info

#Get the main route and connection code between mongo and the app.py 
#def scrape(): #upsert #update (comes first) to retrieve information 
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars_info
    data = scrape_mars.scrape()
    mars.update(
       {},
       data,
       upsert=True
    )
    return redirect("http://localhost:5000/", code=302)

def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True),

