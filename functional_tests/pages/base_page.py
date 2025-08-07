import allure

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """
    Base class for all page objects.

    Purpose:
        - Store common WebDriver actions and helper methods
        - Provide a single place for shared logic across all page objects
        - Simplify child page classes

    Usage:
        from functional_tests.pages.base_page import BasePage
        class MainPage(BasePage):
            pass
    """

    def __init__(self, driver: WebDriver):
        """
        Initialize the base page with a WebDriver instance.

        Args:
            driver (WebDriver): The Selenium WebDriver instance.
        """
        self.driver = driver

    # Common Actions
    def find(self, locator: tuple) -> WebElement:
        """Find a single element."""
        return self.driver.find_element(*locator)

    def click(self, locator: tuple) -> None:
        """Click on an element."""
        self.find(locator).click()

    def get_text(self, locator: tuple) -> str:
        """Get the text content of an element."""
        return self.find(locator).text

    def get_title(self) -> str:
        """Get the current page title."""
        return self.driver.title

    def get_current_url(self) -> str:
        """Get the current page URL."""
        return self.driver.current_url

    # Utilities
    def take_screenshot(self, name: str = "screenshot") -> None:
        """Take a screenshot and attach it to the Allure report."""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
