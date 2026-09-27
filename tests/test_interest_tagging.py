import time
from pages.interest_page import InterestPage


def test_interest_tagging(driver):

    driver.get(
        "https://wonderful-island-090d44a10.7.azurestaticapps.net/"
    )

    interest = InterestPage(driver)

    interest.enter_interest(
        "I want to meet people working on startup ideas"
    )

    interest.click_find_interest()

    result = interest.get_result()

    print("AI Interest Result:", result)

    assert "Networking" in result

    time.sleep(5)