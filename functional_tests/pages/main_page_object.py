import allure

from functional_tests.pages.base_page import BasePage
from functional_tests.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Main Page action methods are here."""

    EXPECTED_TITLE = "Eye-Diskage"
    EXPECTED_URL = "http://localhost:3000/"
    EXPECTED_HEADER = "Eye-Diskage: Django Secret Key Generator"

    @allure.step("Verify page title matches expected")
    def is_title_matches(self) -> bool:
        """Check if the page title matches the expected value."""
        return self.get_title() == self.EXPECTED_TITLE

    @allure.step("Verify page URL matches expected")
    def is_url_matches(self) -> bool:
        """Check if the page URL matches the expected value."""
        return self.get_current_url() == self.EXPECTED_URL

    @allure.step("Check if main header text matches expected")
    def is_main_header_matches(self) -> bool:
        """Verify the main header text matches the expected value."""
        return self.get_text(MainPageLocators.MAIN_HEADER) == self.EXPECTED_HEADER

    @allure.step("Click navigation button: Django Secret Key Gen")
    def click_navigation_button_main(self) -> bool:
        """Click the main nav button and verify URL."""
        self.click(MainPageLocators.NAV_BUTTON_MAIN)
        return self.get_current_url() == "http://localhost:3000/main"

    @allure.step("Click navigation button: Random Number Generator")
    def click_navigation_button_nums(self) -> bool:
        """Click the numbers nav button and verify URL."""
        self.click(MainPageLocators.NAV_BUTTON_NUMS)
        return self.get_current_url() == "http://localhost:3000/random/numbers"

    @allure.step("Click navigation button: Caesar Cipher")
    def click_navigation_button_caesar(self) -> bool:
        """Click the Caesar nav button and verify URL."""
        self.click(MainPageLocators.NAV_BUTTON_CAESAR)
        return self.get_current_url() == "http://localhost:3000/caesar"

    @allure.step("Click navigation button: Vigenère Cipher")
    def click_navigation_button_vigenere(self) -> bool:
        """Click the Vigenère nav button and verify URL."""
        self.click(MainPageLocators.NAV_BUTTON_VIGENERE)
        return self.get_current_url() == "http://localhost:3000/vigenere"

    @allure.step("Click navigation button: Colyte")
    def click_navigation_button_colyte(self) -> bool:
        """Click the Colyte nav button and verify it points to the expected external link."""
        element = self.find(MainPageLocators.NAV_BUTTON_COLYTE)
        element.click()
        return element.get_attribute('href') == "https://colyte.pro/"
