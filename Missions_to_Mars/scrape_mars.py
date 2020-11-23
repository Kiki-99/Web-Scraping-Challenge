#Scraping using Beautiful Soup
# Dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from splinter import Browser



executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# ## NASA Mars News

def scrape():

    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/' 
    browser.visit(url)



    # Scrap the Mars Website
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')




    # Retrieve the parent divs for class 'list text'
    results = soup.find_all('div', class_='list text')


    # Initialize sets of titles and paragraphs
    titles = []
    paragraphs = []

    # for loop to scrape to results
    for result in results:
        # Scrape the news titles
        if result.a:
                title = result.a.text
                titles.append(title)
            
        # Scrape the news paragraphs
        paragraph = result.find('div', class_="article_teaser_body").text
        paragraphs.append(paragraph)
        
        # Print Mars News Data
        print("----------------")
        print(title)
        print(paragraph)


    title = soup.find('div', class_='content_title')
    text = soup.find('div', class_='rollover_description_inner')

    newsTitle = title.text
    newsText = text.text

    print(newsTitle)
    print(newsText)
    time.sleep(2)


    # ## JPL Mars Space Images - Featured Image


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    url_base = 'https://www.jpl.nasa.gov'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    result = soup.find('article', class_='carousel_item').attrs

    print(result)


    style_prop = str(result['style'])
    trim1 = style_prop.replace("background-image:", "")
    trim2 = trim1.replace(" url('", "")
    image = trim2.replace("');", "")
    image_url = url_base + image
    print(image_url)
    time.sleep(2)


    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA22374_hires.jpg'
    browser.visit(featured_image_url)


    # ## Mars Facts


    #Scraping the table and getting HTML string 
    url = "https://space-facts.com/mars/"
    table = pd.read_html(url)[0]
    print(table)



    type(table)



    df = table
    df.columns = ["Parameters", "Values"]
    df.head()



    html_table = df.to_html()
    html_table


    finaltable = html_table.replace('\n', '')
    time.sleep(2)


    # ## Mars Hemispheres


    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    url_base = "https://astrogeology.usgs.gov"

    browser = Browser('chrome', headless=False)
    browser.visit(url)

    soup = BeautifulSoup(browser.html, 'html.parser')

    result = soup.find_all('div', class_="item")

    url_list = []

    for y in result:
        link = y.find('a')['href']
        url_list.append(link)
        
    print("Printing URLs LIST")
    print(url_list)
    print("")
    print("----------------")
    print("Printing 'hemisphere_image_urls' Dictionary")
    print("")

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "..."},
        {"title": "Cerberus Hemisphere", "img_url": "..."},
        {"title": "Schiaparelli Hemisphere", "img_url": "..."},
        {"title": "Syrtis Major Hemisphere", "img_url": "..."},
    ]

    for x in url_list:
        url = url_base + x
            
        browser.visit(url)
        
        #Sleep script to ensure the page fully loads

        
        soup = BeautifulSoup(browser.html, 'html.parser')
        
        # Grab image url
        result1 = soup.find('img', class_="wide-image")
        image = url_base + result1["src"]
        
        # Grab page title and remove "Enhanced" from string
        result2 = soup.find('h2', class_='title')
        title = result2.text
        title = title.rsplit(' ', 1)[0]
        
        mars_hemi = {"title": title, "img_url": image}
        hemisphere_image_urls.append(mars_hemi)
        
    
        
    print(hemisphere_image_urls)

    mars_dictionary = {
        "NewsTitle":newsTitle,
        "NewsText":newsText,
        "ImageURL":image_url,
        "FinalTable":finaltable,
        "HemishpereImageURL":hemisphere_image_urls
    }

    return mars_dictionary

