from functional_tests.pages import main_page_object as page
from functional_tests.tests.test_chrome.base import FunctionalTestChrome


class TestMainPageChrome(FunctionalTestChrome):

    def test_main_page_title(self):
        """Test that Main Page title is correct"""

        main_page = page.MainPage(self.driver)
        self.wait_for(lambda: self.assertTrue(
            main_page.is_title_matches(), 'React App title doesn\'t match.'
            )
        )

    def test_main_page_url(self):
        """Test that URL is correct after opening Main Page"""

        main_page = page.MainPage(self.driver)
        self.wait_for(lambda: self.assertTrue(
            main_page.is_url_matches(),
            'URL does not match after opening Main Page.'
            )
        )

    def test_main_page_header(self):
        """Test that Main Page main header is correct"""

        main_page = page.MainPage(self.driver)
        self.wait_for(lambda: self.assertTrue(
            main_page.is_main_header_matches(),
            'Main Page Header doesn\'t match.'
            )
        )

    def test_navigate_button_click(self):
        """Test that URL is correct after clicking on navigation button"""

        main_page = page.MainPage(self.driver)
        self.wait_for(lambda: self.assertTrue(
            main_page.click_navigation_button(),
            'URL does not match after clicking navigation to About Page.'
            )
        )

    def test_main_page_sub_header(self):
        """Test that Main Page sub header is correct"""

        main_page = page.MainPage(self.driver)
        self.wait_for(lambda: self.assertTrue(
            main_page.is_sub_header_matches(),
            'Main Page SUB Header doesn\'t match.'
            )
        )

    def test_main_page_no_posts_message(self):
        """Test that Main Page no posts message text is correct"""

        main_page = page.MainPage(self.driver)
        self.wait_for(lambda: self.assertTrue(
            main_page.is_no_posts_message_matches(),
            'Main Page "No Posts Message" doesn\'t match.'
            )
        )

    def test_main_pages_counter(self):
        """Test that Main Page pages counter text is correct"""

        main_page = page.MainPage(self.driver)
        self.wait_for(lambda: self.assertTrue(
            main_page.is_pages_counter_matches(),
            'Main Page Pages Counter doesn\'t match.'
            )
        )

    def test_previous_button_disabled(self):
        """Test that previous button is disabled on Main Page"""

        main_page = page.MainPage(self.driver)
        self.wait_for(lambda: self.assertFalse(
            main_page.disabled_page_previous_button(),
            'Previous button is not disabled on Main Page.'
            )
        )

    def test_next_button_disabled(self):
        """Test that next button is disabled on Main Page"""

        main_page = page.MainPage(self.driver)
        self.wait_for(lambda: self.assertFalse(
            main_page.disabled_page_next_button(),
            'Next button is not disabled on Main Page.'
            )
        )

    def test_footer_text(self):
        """Test that footer text is correct"""

        main_page = page.MainPage(self.driver)
        self.wait_for(lambda: self.assertTrue(
            main_page.is_footer_matches(),
            'Main Page Footer text doesn\'t match.'
            )
        )
