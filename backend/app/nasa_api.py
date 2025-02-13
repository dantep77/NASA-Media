import requests
import os
from dotenv import load_dotenv
from flask import jsonify

load_dotenv()  # Load API key from .env file

NASA_API_URL = "https://images-api.nasa.gov/search"

def search_nasa(query, page):
    url = NASA_API_URL
    params = {"title": query, "media_type": "image", "page": page, "page_size": 12}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return jsonify({
            "items": response.json()["collection"]["items"],
            "count": response.json()["collection"]["metadata"]["total_hits"]
        })

    return {"error": "Failed to fetch data from NASA API"}
