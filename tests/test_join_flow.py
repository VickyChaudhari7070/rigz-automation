from pages.join_page import JoinPage
import time

def test_join_form(driver):
    driver.get("https://wonderful-island-090d44a10.7.azurestaticapps.net/")

    page = JoinPage(driver)

    page.open_join_form()
    page.fill_form()
    page.submit()

    assert "Thank you for showing interest in RigZ!" in page.success_message()
    time.sleep(5)