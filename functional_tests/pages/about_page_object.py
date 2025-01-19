from functional_tests.pages.base_page import BasePage
from functional_tests.locators.about_page_locators import AboutPageLocators


class AboutPage(BasePage):
    """About Page action methods are here."""

    def is_title_matches(self):
        """Verifies that the hardcoded text "React App" appears in page title"""

        element = self.driver.find_element(*AboutPageLocators.NAV_BUTTON_ABOUT)
        element.click()
        expected_title = "React App"

        return expected_title == self.driver.title

    def is_url_matches(self):
        """Verifies that the URL is correct on About Page"""

        element = self.driver.find_element(*AboutPageLocators.NAV_BUTTON_ABOUT)
        element.click()
        page_url = 'http://localhost:3000/about'

        return page_url == self.driver.current_url

    def is_main_header_matches(self):
        """Triggers the navigation and checks main header text"""

        element = self.driver.find_element(*AboutPageLocators.NAV_BUTTON_ABOUT)
        element.click()
        element = self.driver.find_element(*AboutPageLocators.MAIN_HEADER)
        expected_header = 'Simple Django and React Blog with Testing Automation'

        return expected_header == element.text

    def click_navigation_button(self):
        """Triggers the navigation button and checks URL"""

        element = self.driver.find_element(*AboutPageLocators.NAV_BUTTON_ABOUT)
        element.click()
        element = self.driver.find_element(*AboutPageLocators.NAV_BUTTON_BLOG)
        element.click()
        page_url = 'http://localhost:3000/main'

        return page_url == self.driver.current_url

    def is_sub_header_matches(self):
        """Triggers the navigation and checks sub header text"""

        element = self.driver.find_element(*AboutPageLocators.NAV_BUTTON_ABOUT)
        element.click()
        element = self.driver.find_element(*AboutPageLocators.SUB_HEADER)
        expected_header = 'About'

        return expected_header == element.text

    def is_pages_counter_matches(self):
        """Triggers the span element and checks pages counter text"""

        element = self.driver.find_element(*AboutPageLocators.NAV_BUTTON_ABOUT)
        element.click()
        element = self.driver.find_element(*AboutPageLocators.PAGES_COUNTER)
        expected_counter = 'Page 1 of 1'

        return expected_counter == element.text

    def redirect_page_return_button(self):
        """Triggers the return button and check is it redirecting"""

        element = self.driver.find_element(*AboutPageLocators.NAV_BUTTON_ABOUT)
        element.click()
        element = self.driver.find_element(*AboutPageLocators.RETURN_BUTTON)
        page_url = 'http://localhost:3000/main'
        element.click()

        return page_url == self.driver.current_url

    def is_footer_matches(self):
        """Triggers the footer element and checks footer text"""

        element = self.driver.find_element(*AboutPageLocators.NAV_BUTTON_ABOUT)
        element.click()
        element = self.driver.find_element(*AboutPageLocators.FOOTER_TEXT)
        expected_footer = '© 2025 by Yehor Romanov @wwwinri aka @pen-alchemist'

        return expected_footer == element.text
