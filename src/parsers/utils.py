import requests


def download_url(url: str) -> str:
    return requests.get(url).text
