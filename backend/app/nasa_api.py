import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file

NASA_API_URL = "https://images-api.nasa.gov/search"

def search_nasa(query, page):
    url = NASA_API_URL
    params = {"q": query, "media_type": "image", "page": page}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()["collection"]["items"]

    return {"error": "Failed to fetch data from NASA API"}
