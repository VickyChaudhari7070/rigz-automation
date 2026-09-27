import time
from pages.join_page import JoinPage


def test_invalid_email(driver):

    driver.get(
        "https://wonderful-island-090d44a10.7.azurestaticapps.net/"
    )

    page = JoinPage(driver)

    page.open_join_form()
    page.fill_form_invalid_email()
    page.submit()

    error = page.get_email_validation_message()

    print("Validation message:", error)

    assert "@" in error

    time.sleep(5)