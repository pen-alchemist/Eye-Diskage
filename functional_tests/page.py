from functional_tests.about_page_locators import AboutPageLocators
from functional_tests.main_page_locators import MainPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Main Page action methods are here."""

    def is_title_matches(self):
        """Verifies that the hardcoded text "React App" appears in page title"""

        expected_title = "React App"

        return expected_title == self.driver.title

    def is_url_matches(self):
        """Verifies that the URL is correct on Main Page"""

        page_url = 'http://localhost:3000/main'

        return page_url == self.driver.current_url

    def is_main_header_matches(self):
        """Triggers the navigation and checks main header text"""

        element = self.driver.find_element(*MainPageLocators.MAIN_HEADER)
        expected_header = 'Simple Django and React Blog with Testing Automation'

        return expected_header == element.text

    def click_navigation_button(self):
        """Triggers the navigation button and checks URL"""

        element = self.driver.find_element(*MainPageLocators.NAV_BUTTON_ABOUT)
        element.click()
        page_url = 'http://localhost:3000/about'

        return page_url == self.driver.current_url

    def is_sub_header_matches(self):
        """Triggers the navigation and checks sub header text"""

        element = self.driver.find_element(*MainPageLocators.SUB_HEADER)
        expected_header = 'All Blogs'

        return expected_header == element.text

    def is_no_posts_message_matches(self):
        """Triggers the header element and checks no posts message text"""

        element = self.driver.find_element(*MainPageLocators.NO_POSTS_MESSAGE)
        expected_message = 'There are no posts!'

        return expected_message == element.text

    def is_pages_counter_matches(self):
        """Triggers the span element and checks pages counter text"""

        element = self.driver.find_element(*MainPageLocators.PAGES_COUNTER)
        expected_counter = 'Page 1 of 1'

        return expected_counter == element.text

    def disabled_page_previous_button(self):
        """Triggers the previous button and check is it disabled"""

        element = self.driver.find_element(*MainPageLocators.PREVIOUS_BUTTON)
        expected_btn_status = element.is_enabled()

        return expected_btn_status

    def disabled_page_next_button(self):
        """Triggers the next button and check is it disabled"""

        element = self.driver.find_element(*MainPageLocators.NEXT_BUTTON)
        expected_btn_status = element.is_enabled()

        return expected_btn_status

    def is_footer_matches(self):
        """Triggers the footer element and checks footer text"""

        element = self.driver.find_element(*MainPageLocators.FOOTER_TEXT)
        expected_footer = '© 2025 by Yehor Romanov @wwwinri aka @pen-alchemist'

        return expected_footer == element.text


class AboutPage(BasePage):
    """About Page action methods are here."""

    def is_title_matches(self):
        """Verifies that the hardcoded text "React App" appears in page title"""

        expected_title = "React App"

        return expected_title == self.driver.title

    def is_url_matches(self):
        """Verifies that the URL is correct on About Page"""

        page_url = 'http://localhost:3000/about'

        return page_url == self.driver.current_url

    def is_main_header_matches(self):
        """Triggers the navigation and checks main header text"""

        element = self.driver.find_element(*AboutPageLocators.MAIN_HEADER)
        expected_header = 'Simple Django and React Blog with Testing Automation'

        return expected_header == element.text

    def click_navigation_button(self):
        """Triggers the navigation button and checks URL"""

        element = self.driver.find_element(*AboutPageLocators.NAV_BUTTON_BLOG)
        element.click()
        page_url = 'http://localhost:3000/main'

        return page_url == self.driver.current_url

    def is_sub_header_matches(self):
        """Triggers the navigation and checks sub header text"""

        element = self.driver.find_element(*AboutPageLocators.SUB_HEADER)
        expected_header = 'About'

        return expected_header == element.text

    def is_no_posts_message_matches(self):
        """Triggers the header element and checks no posts message text"""

        element = self.driver.find_element(*AboutPageLocators.NO_POSTS_MESSAGE)
        expected_message = 'There are no posts!'

        return expected_message == element.text

    def is_pages_counter_matches(self):
        """Triggers the span element and checks pages counter text"""

        element = self.driver.find_element(*AboutPageLocators.PAGES_COUNTER)
        expected_counter = 'Page 1 of 1'

        return expected_counter == element.text

    def disabled_page_return_button(self):
        """Triggers the previous button and check is it disabled"""

        element = self.driver.find_element(*AboutPageLocators.RETURN_BUTTON)
        expected_btn_status = element.is_enabled()

        return expected_btn_status

    def is_footer_matches(self):
        """Triggers the footer element and checks footer text"""

        element = self.driver.find_element(*AboutPageLocators.FOOTER_TEXT)
        expected_footer = '© 2025 by Yehor Romanov @wwwinri aka @pen-alchemist'

        return expected_footer == element.text
