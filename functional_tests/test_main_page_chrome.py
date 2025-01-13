import os
import resource

from django.test.selenium import LiveServerTestCase
from django.contrib.contenttypes.models import ContentType

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from functional_tests import main_page as page


class TestMainPageChrome(LiveServerTestCase):

    def setUp(self):
        """Testing setup. Make the selenium setUp.
        Returns chrome driver"""

        # Clear all cache at once for all cases
        ContentType.objects.clear_cache()

        service = Service(f'{os.getcwd()}/chromedriver')

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
        """Test that blogs page header is correct"""

        main_page = page.MainPage(self.driver)
        self.assertTrue(
            main_page.is_header_matches(), 'Main Page Header doesn\'t match.'
        )

    def test_navigate_button_click(self):
        """Test that URL is correct after clicking on navigation button"""

        main_page = page.MainPage(self.driver)
        self.assertTrue(
            main_page.click_navigation_button(),
            'URL does not match after clicking navigation to About Page.'
        )
