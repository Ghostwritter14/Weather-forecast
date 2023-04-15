import requests


API_Key = "c64d7c8b5b8878cd6b8cf4dcc8ba3f6a"

def get_data(place, forecast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_Key}"
    response = requests.get(url)
    data = response.json()
    filtered = data["list"]
    nr_values = 8 * forecast_days
    filtered = filtered[:nr_values]

    return filtered



