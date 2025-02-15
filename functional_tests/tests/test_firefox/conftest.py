import os
import time
import pytest
import resource

from datetime import datetime

from django.contrib.contenttypes.models import ContentType

from selenium import webdriver
from selenium.common import WebDriverException

from eye_diskage.settings import BASE_DIR
from test_logs.setup_test_logger import logger


@pytest.fixture(scope="module")
def gecko_driver():
    """Fixture to initialize and tear down the Firefox driver."""
    # Clear all cache at once for all cases
    ContentType.objects.clear_cache()

    install_dir = "/snap/firefox/current/usr/lib/firefox"
    driver_loc = os.path.join(install_dir, "geckodriver")
    binary_loc = os.path.join(install_dir, "firefox")

    service = webdriver.FirefoxService(driver_loc)
    opts = webdriver.FirefoxOptions()
    opts.binary_location = binary_loc
    driver = webdriver.Firefox(service=service, options=opts)
    driver.get('http://localhost:3000/')

    yield driver

    # Teardown
    ContentType.objects.clear_cache()
    print('Cache was cleared')

    mb_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
    print(f'Memory usage: {mb_memory} MB')
    logger.info(f'Memory usage: {mb_memory} MB')

    driver.quit()
    print('All testing data was cleared')


@pytest.fixture
def wait_for(gecko_driver):
    """Fixture to wait for a condition to be met, supporting both functions and assertions."""

    def _wait_for(condition, message=None):
        """
        Wait for a condition to be met.

        Args:
            condition: A function or lambda that returns a boolean or raises an AssertionError.
            message (str): Optional custom error message to log if the condition fails.
        """
        MAX_WAIT = 10
        start_time = time.time()

        while True:
            try:
                # If the condition is a function, evaluate it
                if callable(condition):
                    result = condition()
                    if not result:
                        raise AssertionError(message or "Condition not met")
                    return result
                # If the condition is a boolean, check it directly
                elif isinstance(condition, bool):
                    if not condition:
                        raise AssertionError(message or "Condition not met")
                    return condition
                else:
                    raise ValueError("Condition must be a callable or a boolean")
            except (AssertionError, WebDriverException) as error:
                if time.time() - start_time > MAX_WAIT:
                    logger.error(f'ERROR (WAITING CAUGHT ERROR): {error}')
                    time_now = datetime.now()
                    gecko_driver.save_screenshot(f'{BASE_DIR}/test_logs/test-failed-{time_now}.png')
                    raise error
                time.sleep(0.5)

    return _wait_for
