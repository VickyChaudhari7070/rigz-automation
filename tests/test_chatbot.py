import time
from pages.chatbot_page import ChatbotPage


def test_chatbot(driver):

    driver.get(
        "https://wonderful-island-090d44a10.7.azurestaticapps.net/"
    )

    chatbot = ChatbotPage(driver)

    chatbot.open_chatbot()
    chatbot.click_what_is_rigz()

    response = chatbot.get_response()

    print("Chatbot response:", response)

    assert "RigZ helps people reconnect" in response

    time.sleep(5)