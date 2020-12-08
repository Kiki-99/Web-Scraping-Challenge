# Mission to Mars Web Scraping App Challenge
A web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

Files:

Mission_to_mars.ipynb ---> Jupyter Notebook that houses original scrape code for entire project.

Scrape_mars.py ---> Python File that contains two functions; init_browser() (to initiate the browser via chromedriver) and scrape() (to perform scrape of all pages taken from original Jupyter Notebook).

App.py ---> Python/Flask App that utilizes scrape() function from scrape_mars.py to update mars_app DB collection in MongoDB and load as webpage from index.html.

Templates(Folder) ---> HTML webpage used for Mission to Mars that displays the information from our web application scrape.

Screenshots(Folder) ---> Four total JPG images of the Mission to Mars web HTML web page app.

How to use:
In order to run application, please navigate to directory via console. Run app.py as Python file.
