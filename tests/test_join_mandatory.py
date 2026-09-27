import time
from pages.join_page import JoinPage


def test_name_mandatory(driver):

    driver.get(
        "https://wonderful-island-090d44a10.7.azurestaticapps.net/"
    )

    page = JoinPage(driver)

    page.open_join_form()
    page.fill_form_without_name()
    page.submit()

    error = page.get_name_validation_message()

    print("Validation message:", error)

    assert "Please fill out this field" in error

    time.sleep(5)