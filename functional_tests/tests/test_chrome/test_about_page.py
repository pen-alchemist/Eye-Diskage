from functional_tests.pages import about_page_object as page
from functional_tests.tests.test_chrome.base import FunctionalTestChrome


class TestAboutPageChrome(FunctionalTestChrome):

    def test_about_page_title(self):
        """Test that About Page title is correct"""

        about_page = page.AboutPage(self.driver)
        self.wait_for(lambda: self.assertTrue(
            about_page.is_title_matches(), 'React App title doesn\'t match.'
            )
        )

    def test_main_page_url(self):
        """Test that URL is correct after opening About Page"""

        about_page = page.AboutPage(self.driver)
        self.wait_for(lambda: self.assertTrue(
            about_page.is_url_matches(),
            'URL does not match after opening About Page.'
            )
        )

    def test_main_page_header(self):
        """Test that About Page main header is correct"""

        about_page = page.AboutPage(self.driver)
        self.wait_for(lambda: self.assertTrue(
            about_page.is_main_header_matches(),
            'About Page Header doesn\'t match.'
            )
        )

    def test_navigate_button_click(self):
        """Test that URL is correct after clicking on navigation button"""

        about_page = page.AboutPage(self.driver)
        self.wait_for(lambda: self.assertTrue(
            about_page.click_navigation_button(),
            'URL does not match after clicking navigation to About Page.'
            )
        )

    def test_about_page_sub_header(self):
        """Test that About Page sub header is correct"""

        about_page = page.AboutPage(self.driver)
        self.wait_for(lambda: self.assertTrue(
            about_page.is_sub_header_matches(),
            'About Page SUB Header doesn\'t match.'
            )
        )

    def test_return_button_redirect(self):
        """Test that return button is redirecting to the Main Page"""

        about_page = page.AboutPage(self.driver)
        self.wait_for(lambda: self.assertTrue(
            about_page.redirect_page_return_button(),
            'Return button is not enabled on About Page.'
            )
        )

    def test_footer_text(self):
        """Test that footer text is correct"""

        about_page = page.AboutPage(self.driver)
        self.wait_for(lambda: self.assertTrue(
            about_page.is_footer_matches(),
            'About Page Footer text doesn\'t match.'
            )
        )
