import os
import time
import pytest
import resource
import allure

from datetime import datetime
from typing import Callable, Union

from django.contrib.contenttypes.models import ContentType

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common import WebDriverException

from eye_diskage.settings import BASE_DIR
from test_logs.setup_test_logger import logger


def pytest_configure(config):
    """Register custom marks to avoid pytest warnings."""
    config.addinivalue_line("markers", "ui: mark test as a UI test needing a browser")


@pytest.fixture(scope="module", params=["chrome", "firefox"])
def browser_driver(request):
    """
    Fixture to initialize and tear down browser drivers (Chrome/Firefox).
    """
    browser_name = request.param
    ContentType.objects.clear_cache()
    logger.info("Django ContentType cache cleared before test run.")

    if browser_name == "chrome":
        # Note: falling back to webdriver auto-management using Selenium 4.x
        # or relying on PATH if no specific chromedriver exists locally.
        # But for compatibility, defining it like the previous file:
        service = ChromeService(f"{BASE_DIR}/functional_tests/tests/test_chrome/chromedriver")
        options = ChromeOptions()
        options.add_argument("--disable-extensions")
        options.add_argument("--start-maximized")
        # For CI/CD
        # options.add_argument("--headless=new")

        logger.info("Starting Chrome WebDriver...")
        try:
            driver = webdriver.Chrome(service=service, options=options)
        except Exception:
            # Fallback for when the explicit executable is missing (e.g., Selenium Managers handles it)
            driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        install_dir = "/snap/firefox/current/usr/lib/firefox"
        driver_loc = os.path.join(install_dir, "geckodriver")
        binary_loc = os.path.join(install_dir, "firefox")

        logger.info("Starting Firefox WebDriver...")
        try:
            service = webdriver.FirefoxService(driver_loc)
            options = webdriver.FirefoxOptions()
            options.binary_location = binary_loc
            # options.add_argument("--headless")
            driver = webdriver.Firefox(service=service, options=options)
        except Exception:
            # Fallback for systems without snap Firefox / geckodriver hardcoded paths
            driver = webdriver.Firefox()

    try:
        test_url = "http://localhost:3000/"
        logger.info(f"Navigating to {test_url}")
        driver.get(test_url)
        yield driver
    finally:
        ContentType.objects.clear_cache()
        logger.info("Django ContentType cache cleared after test run.")

        try:
            # This is specific to Unix, so adding a safety guard around it.
            mb_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
            logger.info(f"Memory usage: {mb_memory:.2f} MB")
            allure.attach(str(mb_memory), "Memory Usage (MB)", allure.attachment_type.TEXT)
        except AttributeError:
            pass # Windows or system without `resource` compatibility

        try:
            driver.quit()
            logger.info(f"{browser_name.capitalize()} WebDriver session ended.")
        except Exception as e:
            logger.error(f"Error quitting {browser_name} driver: {e}")

        print("All testing data was cleared.")


@pytest.fixture
def wait_for(browser_driver):
    """
    Wait for a condition to be met within a maximum time.
    """

    def _wait_for(condition: Union[Callable[[], bool], bool], message: str = None):
        MAX_WAIT = 10
        start_time = time.time()

        while True:
            try:
                if callable(condition):
                    result = condition()
                    if not result:
                        raise AssertionError(message or "Condition not met")
                    return result
                elif isinstance(condition, bool):
                    if not condition:
                        raise AssertionError(message or "Condition not met")
                    return condition
                else:
                    raise ValueError("Condition must be callable or boolean")
            except (AssertionError, WebDriverException) as error:
                if time.time() - start_time > MAX_WAIT:
                    logger.error(f"WAIT ERROR: {error}")
                    time_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    screenshot_path = f"{BASE_DIR}/test_logs/test-failed-{time_now}.png"
                    browser_driver.save_screenshot(screenshot_path)

                    allure.attach.file(
                        screenshot_path,
                        name=f"Failure Screenshot - {time_now}",
                        attachment_type=allure.attachment_type.PNG
                    )
                    raise
                time.sleep(0.5)

    return _wait_for
