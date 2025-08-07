from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Centralized collection of locators for the Main Page.

    Purpose:
        - Maintain all Main Page locators in a single location
        - Prevent selector duplication in page objects or tests
        - Improve maintainability and readability for the test suite

    Usage:
        from functional_tests.locators.main_page_locators import MainPageLocators
        driver.find_element(*MainPageLocators.NAV_BUTTON_MAIN).click()
    """

    # Navigation Buttons
    NAV_BUTTON_MAIN = (By.LINK_TEXT, "Django Secret Key Gen")
    NAV_BUTTON_NUMS = (By.LINK_TEXT, "Random Number Generator")
    NAV_BUTTON_CAESAR = (By.LINK_TEXT, "Caesar Cipher")
    NAV_BUTTON_VIGENERE = (By.LINK_TEXT, "Vigenère Cipher")
    NAV_BUTTON_COLYTE = (By.LINK_TEXT, "Colyte")

    # Headers
    MAIN_HEADER = (By.ID, "main-header2")
    SUB_HEADER = (By.TAG_NAME, "h1")

    # Footer
    FOOTER_TEXT = (By.CLASS_NAME, "footer")
