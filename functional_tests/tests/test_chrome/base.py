import time
import resource

from datetime import datetime

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.contenttypes.models import ContentType

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common import WebDriverException

from eye_diskage.settings import BASE_DIR
from test_logs.setup_test_logger import logger


class FunctionalTestChrome(StaticLiveServerTestCase):

    def setUp(self):
        """Testing setup. Make the selenium setUp.
        Returns chrome driver"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()

        service = Service(
            f'{BASE_DIR}/functional_tests/tests/test_chrome/chromedriver'
        )

        # Create Chrome Options object
        options = Options()
        options.add_argument("--disable-extensions")

        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/')

    def tearDown(self):
        """Testing teardown. Driver quit (browser quit)"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()
        print('Cache was cleared')

        mb_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
        print(f'Memory usage: {mb_memory} MB')
        logger.info(f'Memory usage: {mb_memory} MB')

        self.driver.quit()

        print('All testing data was cleared')

    def wait_for(self, fn):
        """Average waiting maximum 10 until
        success try or got error and time is left"""

        MAX_WAIT = 10
        start_time = time.time()

        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as error:
                if time.time() - start_time > MAX_WAIT:
                    logger.error(
                        f'ERROR (WAITING CAUGHT ERROR): {error}'
                    )
                    time_now = datetime.now()
                    self.driver.save_screenshot(
                        f'{BASE_DIR}/test_logs/test-failed-{time_now}.png'
                    )

                    raise error
                time.sleep(0.5)
