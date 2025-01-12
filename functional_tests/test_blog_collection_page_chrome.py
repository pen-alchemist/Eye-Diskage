import os
import resource

from django.test.selenium import LiveServerTestCase
from django.contrib.contenttypes.models import ContentType

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from functional_tests import blog_collection_page as page


class TestAllBlogsPageChrome(LiveServerTestCase):

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

    def test_posts_all_page_title(self):
        """Test that blogs page title is correct"""

        # Load the main page. In this case the home page of Blog.
        main_page = page.MainPage(self.driver)
        # Checks if the word "React App" is in title
        self.assertTrue(main_page.is_title_matches(), 'React App title doesn\'t match.')
