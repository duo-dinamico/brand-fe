import requests

base_url = "https://brands.duodinamico.online"


def get_brands() -> dict[str, list]:
    return requests.get(f"{base_url}/brands")
