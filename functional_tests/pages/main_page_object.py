from functional_tests.pages.base_page import BasePage
from functional_tests.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Main Page action methods are here."""

    def is_title_matches(self):
        """Verifies that the hardcoded text "React App" appears in page title"""

        expected_title = "Eye-Diskage"

        return expected_title == self.driver.title

    def is_url_matches(self):
        """Verifies that the URL is correct on Main Page"""

        page_url = 'http://localhost:3000/'

        return page_url == self.driver.current_url

    def is_main_header_matches(self):
        """Triggers the navigation and checks main header text"""

        element = self.driver.find_element(*MainPageLocators.MAIN_HEADER)
        expected_header = 'Eye-Diskage: Django Secret Key Generator'

        return expected_header == element.text

    def click_navigation_button_main(self):
        """Triggers the navigation button and checks URL"""

        element = self.driver.find_element(*MainPageLocators.NAV_BUTTON_MAIN)
        element.click()
        page_url = 'http://localhost:3000/main'

        return page_url == self.driver.current_url

    def click_navigation_button_nums(self):
        """Triggers the navigation button and checks URL"""

        element = self.driver.find_element(*MainPageLocators.NAV_BUTTON_NUMS)
        element.click()
        page_url = 'http://localhost:3000/random/numbers'

        return page_url == self.driver.current_url

    def click_navigation_button_caesar(self):
        """Triggers the navigation button and checks URL"""

        element = self.driver.find_element(*MainPageLocators.NAV_BUTTON_CAESAR)
        element.click()
        page_url = 'http://localhost:3000/caesar'

        return page_url == self.driver.current_url

    def click_navigation_button_vigenere(self):
        """Triggers the navigation button and checks URL"""

        element = self.driver.find_element(*MainPageLocators.NAV_BUTTON_VIGENERE)
        element.click()
        page_url = 'http://localhost:3000/vigenere'

        return page_url == self.driver.current_url

    def click_navigation_button_colyte(self):
        """Triggers the navigation button and checks URL"""

        element = self.driver.find_element(*MainPageLocators.NAV_BUTTON_COLYTE)
        element.click()
        page_url = 'https://colyte.pro/'

        return page_url == element.get_attribute('href')
