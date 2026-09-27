import requests


def test_interest_api():

    url = "https://wonderful-island-090d44a10.7.azurestaticapps.net/api/interest"

    payload = {
        "message": "I want to meet people working on startup ideas"
    }

    response = requests.post(url, json=payload)

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200
    assert response.json()["interest"] == "Networking"