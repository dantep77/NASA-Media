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
        response = response.json()

        #Get items from current page
        all_items.extend(response["collection"]["items"])

        #Check for another page
        print("response", response)
        links = response.get("collection", {}).get("links", [])
        print("collection",response.get("collection", {}))
        print("links", links)
        if links[0].get("prompt") == "Next":
            url = links[0].get("href")
            response = requests.get(url)
        else:
            url = None
        

    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch data from NASA API"}
