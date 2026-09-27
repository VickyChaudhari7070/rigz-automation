from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ChatbotPage(BasePage):

    CHAT_ICON = (
        By.XPATH,
        "//*[normalize-space()='💬']"
    )

    WHAT_IS_RIGZ = (
        By.XPATH,
        "//button[normalize-space()='What is RigZ?']"
    )

    RESPONSE = (
        By.XPATH,
        "//*[contains(text(),'RigZ helps people reconnect')]"
    )

    def open_chatbot(self):
        self.click(self.CHAT_ICON)

    def click_what_is_rigz(self):
        self.click(self.WHAT_IS_RIGZ)

    def get_response(self):
        return self.get_text(self.RESPONSE)