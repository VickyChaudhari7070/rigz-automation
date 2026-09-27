import json
import time

from pages.interest_page import InterestPage


def test_interest_ui_api_integration(driver):

    driver.get(
        "https://wonderful-island-090d44a10.7.azurestaticapps.net/"
    )

    interest = InterestPage(driver)

    # Perform action through UI
    interest.enter_interest(
        "I want to meet people working on startup ideas"
    )

    interest.click_find_interest()

    # Validate UI result
    ui_result = interest.get_result()

    print("UI Result:", ui_result)

    assert "Networking" in ui_result

    # Read Chrome network logs
    logs = driver.get_log("performance")

    api_found = False

    for log in logs:

        message = json.loads(log["message"])["message"]

        if message["method"] == "Network.responseReceived":

            response = message["params"]["response"]
            url = response["url"]

            if "/api/interest" in url:

                print("API URL:", url)
                print("API Status:", response["status"])

                assert response["status"] == 200

                api_found = True
                break

    assert api_found, "Interest API call was not detected"

    time.sleep(5)