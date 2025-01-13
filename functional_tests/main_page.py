from functional_tests.main_page_locators import MainPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Blog Collection Page action methods are here."""

    def is_title_matches(self):
        """Verifies that the hardcoded text "React App" appears in page title"""

        title_text = "React App"

        return title_text == self.driver.title

    def click_navigation_button(self):
        """Triggers the navigation and checks URL (with hardcoded text)"""

        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

        page_url = 'http://localhost:3000/about'

        return page_url == self.driver.current_url
