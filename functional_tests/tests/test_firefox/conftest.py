import os
import time
import pytest
import resource

from datetime import datetime

from django.contrib.contenttypes.models import ContentType

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
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
    service = Service(driver_loc)

    # Create Chrome Options object
    options = Options()
    options.binary_location = binary_loc

    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
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
def wait_for(chrome_driver):
    """Fixture to wait for a condition to be met."""
    def _wait_for(fn):
        MAX_WAIT = 10
        start_time = time.time()

        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as error:
                if time.time() - start_time > MAX_WAIT:
                    logger.error(f'ERROR (WAITING CAUGHT ERROR): {error}')
                    time_now = datetime.now()
                    chrome_driver.save_screenshot(f'{BASE_DIR}/test_logs/test-failed-{time_now}.png')
                    raise error
                time.sleep(0.5)
    return _wait_for
