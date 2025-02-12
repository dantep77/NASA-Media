import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file

NASA_API_URL = "https://images-api.nasa.gov/search"

def search_nasa(query):
    url = NASA_API_URL
    params = {"q": query, "media_type": "image"}
    all_items = []
    response = requests.get(url, params=params)

    while url:
        json = response.json()

        #Get items from current page
        all_items.extend(json["collection"]["items"])

        #Check for another page
        links = json.get("collection", {}).get("links", [])
    
        if len(links) > 0:
            url = links[0].get("href")
            response = requests.get(url)
        else:
            url = None
        

    if response.status_code == 200:
        return all_items
    return {"error": "Failed to fetch data from NASA API"}
