import requests
from typing import Optional

base_url = "https://brands.duodinamico.online"


def post_login(username: str, password: str):
    return requests.post(f"{base_url}/login", data={"username": username, "password": password})


def post_signup(username: str, password: str, email: Optional[str]):
    return requests.post(f"{base_url}/signup", json={"username": username, "password": password, "email": email})
