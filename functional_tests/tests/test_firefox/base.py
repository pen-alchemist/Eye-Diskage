import os
import time
import resource

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.contenttypes.models import ContentType

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.common import WebDriverException


class FunctionalTestFirefox(StaticLiveServerTestCase):

    def setUp(self):
        """Testing setup. Make the selenium setUp.
        Returns firefox driver"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()

        install_dir = "/snap/firefox/current/usr/lib/firefox"
        driver_loc = os.path.join(install_dir, "geckodriver")
        binary_loc = os.path.join(install_dir, "firefox")
        service = Service(driver_loc)

        # Create Chrome Options object
        options = Options()
        options.binary_location = binary_loc

        self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/')

    def tearDown(self):
        """Testing teardown. Driver quit (browser quit)"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()
        print('Cache was cleared')

        mb_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
        print(f'Memory usage: {mb_memory} MB')

        self.driver.quit()

        print('All testing data was cleared')

    def wait_for(self, fn):
        """Docstring"""

        MAX_WAIT = 10
        start_time = time.time()

        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as error:
                if time.time() - start_time > MAX_WAIT:
                    raise error
                time.sleep(0.5)
