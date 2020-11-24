from flask import Flask,render_template,redirect
from flask_pymongo import PyMongo 
import scrape_mars

#Get the main route and connection code between mongo and the app.py 
@app.route("/scrape")
def scrape(): #upsert #update (comes first) to retrieve information 

