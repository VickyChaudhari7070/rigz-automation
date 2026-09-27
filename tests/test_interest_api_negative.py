import requests


def test_interest_api_empty_message():

    url = "https://wonderful-island-090d44a10.7.azurestaticapps.net/api/interest"

    payload = {
        "message": ""
    }

    response = requests.post(url, json=payload)

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    # Expected API behaviour
    assert response.status_code == 400