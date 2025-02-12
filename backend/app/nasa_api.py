import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file

NASA_API_URL = "https://images-api.nasa.gov/search"

def search_nasa(query):
    params = {"q": query, "media_type": "image"}
    response = requests.get(NASA_API_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch data from NASA API"}
