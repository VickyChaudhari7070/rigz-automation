from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class JoinPage(BasePage):

    # Locators - keep these inside the class
    JOIN = (By.XPATH, "//a[contains(.,'Join the Journey')]")
    NAME = (By.XPATH, "//label[contains(.,'Full Name')]/following::input[1]")
    EMAIL = (By.XPATH, "//label[contains(.,'Email Address')]/following::input[1]")
    CONTACT = (By.XPATH, "//label[contains(.,'Contact Number')]/following::input[1]")
    LINKEDIN = (By.XPATH, "//label[contains(.,'LinkedIn Profile')]/following::input[1]")
    MESSAGE = (By.XPATH, "//label[contains(.,'Message')]/following::textarea[1]")
    SUBMIT = (By.XPATH, "//button[contains(.,'Submit')]")
    SUCCESS = (
        By.XPATH,
        "//*[contains(text(),'Thank you for showing interest in RigZ!')]"
    )

    # Methods - also inside the class
    def open_join_form(self):
        self.click(self.JOIN)

    def fill_form(self):
        self.type(self.NAME, "RigZ Automation")
        self.type(self.EMAIL, "rigztest@gmail.com")
        self.type(self.CONTACT, "9999999999")
        self.type(self.LINKEDIN, "https://linkedin.com/in/rigztest")
        self.type(self.MESSAGE, "Automation test")

    def submit(self):
        self.click(self.SUBMIT)

    def success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS)
        ).text

    def fill_form_invalid_email(self):
        self.type(self.NAME, "Test Student")
        self.type(self.EMAIL, "abc")
        self.type(self.CONTACT, "9999999999")
        self.type(self.LINKEDIN, "https://linkedin.com/in/test")
        self.type(self.MESSAGE, "Testing invalid email")

    def get_email_validation_message(self):
        email = self.driver.find_element(*self.EMAIL)
        return email.get_attribute("validationMessage")

    def fill_form_without_name(self):
        self.type(self.EMAIL, "rigztest@gmail.com")
        self.type(self.CONTACT, "9999999999")
        self.type(self.LINKEDIN, "https://linkedin.com/in/test")
        self.type(self.MESSAGE, "Testing mandatory field")

    def get_name_validation_message(self):
        name = self.driver.find_element(*self.NAME)
        return name.get_attribute("validationMessage")