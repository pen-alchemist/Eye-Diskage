from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    NAV_BUTTON_MAIN = (By.LINK_TEXT, 'Django Secret Key Gen')
    NAV_BUTTON_NUMS = (By.LINK_TEXT, 'Random Number Generator')
    NAV_BUTTON_CAESAR = (By.LINK_TEXT, 'Caesar Cipher')
    NAV_BUTTON_VIGENERE = (By.LINK_TEXT, 'Vigenère Cipher')
    NAV_BUTTON_COLYTE = (By.LINK_TEXT, 'Colyte')
    MAIN_HEADER = (By.ID, 'main-header2')
    SUB_HEADER = (By.TAG_NAME, 'h1')
    FOOTER_TEXT = (By.CLASS_NAME, 'footer')
