class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Blog Collection Page action methods are here."""

    def is_title_matches(self):
        """Verifies that the hardcoded text "React App" appears in page title"""

        return "React App" in self.driver.title
