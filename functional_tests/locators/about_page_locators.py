from selenium.webdriver.common.by import By


class AboutPageLocators:
    """
    Centralized collection of locators for the About Page.

    Purpose:
        - Store all locator definitions in one place for maintainability
        - Avoid hardcoding selectors inside page objects or tests
        - Provide clear, self-documenting constants for UI elements

    Usage:
        from functional_tests.locators.about_page_locators import AboutPageLocators
        driver.find_element(*AboutPageLocators.NAV_BUTTON_ABOUT).click()
    """

    # Navigation Buttons
    NAV_BUTTON_BLOG = (By.ID, "nav-button-eye_diskage")
    NAV_BUTTON_ABOUT = (By.ID, "nav-button-about")

    # Headers & Messages
    MAIN_HEADER = (By.ID, "main-header2")
    SUB_HEADER = (By.TAG_NAME, "h1")
    NO_POSTS_MESSAGE = (By.CLASS_NAME, "no-posts")

    # Pagination & Navigation
    PAGES_COUNTER = (By.ID, "pages-counter")
    RETURN_BUTTON = (By.XPATH, "//button[span[text()='Return to Blog']]")

    # Footer
    FOOTER_TEXT = (By.CLASS_NAME, "footer")
