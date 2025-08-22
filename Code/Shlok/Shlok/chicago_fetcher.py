import requests

def fetch_chicago_violations(limit=5):
    url = f"https://data.cityofchicago.org/resource/4ijn-s7e5.json?$limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []   

def search_chicago_violations(query, limit=10):
    url = f"https://data.cityofchicago.org/resource/4ijn-s7e5.json?$q={query}&$limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []
