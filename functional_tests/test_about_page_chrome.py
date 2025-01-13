import os
import resource

from django.test.selenium import LiveServerTestCase
from django.contrib.contenttypes.models import ContentType

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from functional_tests import page


class TestAboutPageChrome(LiveServerTestCase):

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

    def test_about_page_title(self):
        """Test that About Page title is correct"""

        about_page = page.AboutPage(self.driver)
        self.assertTrue(
            about_page.is_title_matches(), 'React App title doesn\'t match.'
        )

    def test_main_page_url(self):
        """Test that URL is correct after opening About Page"""

        about_page = page.AboutPage(self.driver)
        self.assertTrue(
            about_page.is_url_matches(),
            'URL does not match after opening About Page.'
        )

    def test_main_page_header(self):
        """Test that About Page main header is correct"""

        about_page = page.AboutPage(self.driver)
        self.assertTrue(
            about_page.is_main_header_matches(),
            'About Page Header doesn\'t match.'
        )

    def test_navigate_button_click(self):
        """Test that URL is correct after clicking on navigation button"""

        about_page = page.AboutPage(self.driver)
        self.assertTrue(
            about_page.click_navigation_button(),
            'URL does not match after clicking navigation to About Page.'
        )

    def test_about_page_sub_header(self):
        """Test that About Page sub header is correct"""

        about_page = page.AboutPage(self.driver)
        self.assertTrue(
            about_page.is_sub_header_matches(),
            'About Page SUB Header doesn\'t match.'
        )

    def test_about_page_no_posts_message(self):
        """Test that About Page no posts message text is correct"""

        about_page = page.AboutPage(self.driver)
        self.assertTrue(
            about_page.is_no_posts_message_matches(),
            'About Page "No Posts Message" doesn\'t match.'
        )

    def test_previous_button_disabled(self):
        """Test that previous button is disabled on About Page"""

        about_page = page.AboutPage(self.driver)
        self.assertFalse(
            about_page.disabled_page_return_button(),
            'Return button is not enabled on About Page.'
        )

    def test_footer_text(self):
        """Test that footer text is correct"""

        about_page = page.AboutPage(self.driver)
        self.assertTrue(
            about_page.is_footer_matches(),
            'About Page Footer text doesn\'t match.'
        )
