import os
import resource

from django.test.selenium import LiveServerTestCase
from django.contrib.contenttypes.models import ContentType

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from functional_tests import main_page as page


class TestMainPageFirefox(LiveServerTestCase):

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

    def test_main_page_title(self):
        """Test that blogs page title is correct"""

        main_page = page.MainPage(self.driver)
        self.assertTrue(
            main_page.is_title_matches(), 'React App title doesn\'t match.'
        )

    def test_main_page_url(self):
        """Test that URL is correct after opening Main Page"""

        main_page = page.MainPage(self.driver)
        self.assertTrue(
            main_page.is_url_matches(),
            'URL does not match after opening Main Page.'
        )

    def test_main_page_header(self):
        """Test that blogs page main header is correct"""

        main_page = page.MainPage(self.driver)
        self.assertTrue(
            main_page.is_main_header_matches(),
            'Main Page Header doesn\'t match.'
        )

    def test_navigate_button_click(self):
        """Test that URL is correct after clicking on navigation button"""

        main_page = page.MainPage(self.driver)
        self.assertTrue(
            main_page.click_navigation_button(),
            'URL does not match after clicking navigation to About Page.'
        )

    def test_main_page_sub_header(self):
        """Test that blogs page sub header is correct"""

        main_page = page.MainPage(self.driver)
        self.assertTrue(
            main_page.is_sub_header_matches(),
            'Main Page SUB Header doesn\'t match.'
        )
