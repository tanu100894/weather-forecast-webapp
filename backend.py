from dotenv import load_dotenv
import os, requests

# Load environment variable from .env file
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv("api_key")

def get_data(place, forecast_days):
    url = (f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}")
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))