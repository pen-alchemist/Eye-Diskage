from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    NAV_BUTTON_BLOG = (By.ID, 'nav-button-blog')
    NAV_BUTTON_ABOUT = (By.ID, 'nav-button-about')
    MAIN_HEADER = (By.ID, 'main-header2')
    SUB_HEADER = (By.TAG_NAME, 'h1')
    NO_POSTS_MESSAGE = (By.CLASS_NAME, 'no-posts')
    PAGES_COUNTER = (By.ID, 'pages-counter')
    PREVIOUS_BUTTON = (By.XPATH, '//button[span[text()=\'Previous\']]')
    NEXT_BUTTON = (By.XPATH, '//button[span[text()=\'Next\']]')
