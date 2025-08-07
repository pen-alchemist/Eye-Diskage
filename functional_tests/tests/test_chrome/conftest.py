import time
import pytest
import resource
import allure

from datetime import datetime
from typing import Callable, Union

from django.contrib.contenttypes.models import ContentType

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common import WebDriverException

from eye_diskage.settings import BASE_DIR
from test_logs.setup_test_logger import logger


@pytest.fixture(scope="module")
def chrome_driver():
    """
    Fixture to initialize and tear down the Chrome driver.

    This fixture:
    - Clears Django ContentType cache before and after tests
    - Launches a maximized Chrome browser
    - Navigates to the test base URL
    - Logs memory usage after execution
    - Attaches diagnostic info to Allure reports
    """
    ContentType.objects.clear_cache()
    logger.info("Django ContentType cache cleared before test run.")

    service = Service(f"{BASE_DIR}/functional_tests/tests/test_chrome/chromedriver")
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")
    # For CI/CD
    # options.add_argument("--headless=new")

    logger.info("Starting Chrome WebDriver...")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        test_url = "http://localhost:3000/"
        logger.info(f"Navigating to {test_url}")
        driver.get(test_url)
        yield driver
    finally:
        ContentType.objects.clear_cache()
        logger.info("Django ContentType cache cleared after test run.")

        mb_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
        logger.info(f"Memory usage: {mb_memory:.2f} MB")
        allure.attach(str(mb_memory), "Memory Usage (MB)", allure.attachment_type.TEXT)

        try:
            driver.quit()
            logger.info("Chrome WebDriver session ended.")
        except Exception as e:
            logger.error(f"Error quitting driver: {e}")

        print("All testing data was cleared.")


@pytest.fixture
def wait_for(chrome_driver):
    """
    Wait for a condition to be met within a maximum time.

    Args:
        chrome_driver: WebDriver instance (provided by pytest fixture)

    Returns:
        Callable that accepts:
            - condition: Callable[[], bool] or bool
            - message: Optional[str] for assertion error message
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
                    chrome_driver.save_screenshot(screenshot_path)

                    allure.attach.file(
                        screenshot_path,
                        name=f"Failure Screenshot - {time_now}",
                        attachment_type=allure.attachment_type.PNG
                    )
                    raise
                time.sleep(0.5)

    return _wait_for
