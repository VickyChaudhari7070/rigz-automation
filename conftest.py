import os
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):

    options = webdriver.ChromeOptions()

    options.set_capability(
        "goog:loggingPrefs",
        {"performance": "ALL"}
    )

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver

    # Take screenshot only if test FAILED
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        os.makedirs("reports/screenshots", exist_ok=True)

        screenshot_path = (
            f"reports/screenshots/{request.node.name}.png"
        )

        driver.save_screenshot(screenshot_path)

        print(f"Failure screenshot: {screenshot_path}")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)