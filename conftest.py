import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import yaml
from datetime import datetime


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def test_data():
    with open("data/test_data.yaml", "r") as file:
        data = yaml.safe_load(file)
    return data

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks first
    outcome = yield
    report = outcome.get_result()

    # When test fails
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser")  # get browser fixture
        if driver:
            # filename format: test_name_20250118_140312.png
            screenshots = "screenshots"
            if not os.path.exists(screenshots):
                os.makedirs(screenshots)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{report.nodeid.replace('::', '_')}_{timestamp}.png"
            screenshot_path = os.path.join(screenshots, screenshot_name)

            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved to: {screenshot_path}")

