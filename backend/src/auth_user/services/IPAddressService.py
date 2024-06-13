import requests


def get_ip():
    response = requests.get('https://api64.ipify.org/?format=json')
    if response.status_code == 200:
        return response.json().get('ip')
    else:
        return None


def get_country_and_city(ip_address):
    response = requests.post(f'https://ipapi.co/{ip_address}/json/')
    if response.status_code == 200:
        data = response.json()
        return f"{data.get('country_name', '')}, {data.get('city', '')}"
    else:
        return None
