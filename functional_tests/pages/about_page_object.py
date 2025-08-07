from selenium.webdriver.remote.webelement import WebElement

from functional_tests.pages.base_page import BasePage
from functional_tests.locators.about_page_locators import AboutPageLocators


class AboutPage(BasePage):
    """
    Page Object Model for the About Page.

    Purpose:
        - Encapsulate About Page UI interactions
        - Provide reusable, readable methods for tests
        - Avoid hardcoding selectors and text in test cases

    Usage:
        about_page = AboutPage(driver)
        assert about_page.is_title_matches()
    """

    BASE_URL = "http://localhost:3000"
    EXPECTED_TITLE = "React App"
    EXPECTED_HEADER = "Simple Django and React Blog with Testing Automation"
    EXPECTED_SUB_HEADER = "About"
    EXPECTED_COUNTER = "Page 1 of 1"
    EXPECTED_FOOTER = "© 2025 by Yehor Romanov @wwwinri aka @pen-alchemist"

    # Navigation Helpers
    def _navigate_to_about(self) -> None:
        """Click the About navigation button."""
        self.driver.find_element(*AboutPageLocators.NAV_BUTTON_ABOUT).click()

    def _click_element(self, locator: tuple) -> WebElement:
        """Click an element and return it."""
        element = self.driver.find_element(*locator)
        element.click()
        return element

    # Assertions
    def is_title_matches(self) -> bool:
        """Verify that the page title matches the expected About page title."""
        self._navigate_to_about()
        return self.EXPECTED_TITLE == self.driver.title

    def is_url_matches(self) -> bool:
        """Verify that the About Page URL is correct."""
        self._navigate_to_about()
        return f"{self.BASE_URL}/about" == self.driver.current_url

    def is_main_header_matches(self) -> bool:
        """Verify that the main header text matches the expected value."""
        self._navigate_to_about()
        header = self.driver.find_element(*AboutPageLocators.MAIN_HEADER)
        return self.EXPECTED_HEADER == header.text

    def click_navigation_button(self) -> bool:
        """
        Click the About navigation button,
        then click Blog button and verify redirection to Main page.
        """
        self._navigate_to_about()
        self._click_element(AboutPageLocators.NAV_BUTTON_BLOG)
        return f"{self.BASE_URL}/main" == self.driver.current_url

    def is_sub_header_matches(self) -> bool:
        """Verify that the sub-header matches the expected About page sub-header."""
        self._navigate_to_about()
        sub_header = self.driver.find_element(*AboutPageLocators.SUB_HEADER)
        return self.EXPECTED_SUB_HEADER == sub_header.text

    def is_pages_counter_matches(self) -> bool:
        """Verify that the pages counter text matches the expected value."""
        self._navigate_to_about()
        counter = self.driver.find_element(*AboutPageLocators.PAGES_COUNTER)
        return self.EXPECTED_COUNTER == counter.text

    def redirect_page_return_button(self) -> bool:
        """Click the return button and verify redirection to the Main page."""
        self._navigate_to_about()
        self._click_element(AboutPageLocators.RETURN_BUTTON)
        return f"{self.BASE_URL}/main" == self.driver.current_url

    def is_footer_matches(self) -> bool:
        """Verify that the footer text matches the expected value."""
        self._navigate_to_about()
        footer = self.driver.find_element(*AboutPageLocators.FOOTER_TEXT)
        return self.EXPECTED_FOOTER == footer.text
