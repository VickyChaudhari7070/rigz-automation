from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InterestPage(BasePage):

    INTEREST_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'I want to meet people')]"
    )

    FIND_INTEREST = (
        By.XPATH,
        "//button[contains(.,'Find My Interest')]"
    )

    RESULT = (
        By.XPATH,
        "//*[contains(text(),'Best match:')]"
    )

    def enter_interest(self, text):
        self.type(self.INTEREST_INPUT, text)

    def click_find_interest(self):
        self.click(self.FIND_INTEREST)

    def get_result(self):
        return self.get_text(self.RESULT)