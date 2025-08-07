import allure
import pytest

from functional_tests.pages import main_page_object as page


@allure.epic("Main Page Tests")
@allure.feature("UI and Navigation")
class TestMainPage:

    @allure.story("Title Verification")
    @allure.title("Verify Main Page Title is Correct")
    def test_main_page_title(self, gecko_driver, wait_for):
        main_page = page.MainPage(gecko_driver)
        with allure.step("Verify the title matches the expected value"):
            wait_for(
                lambda: main_page.is_title_matches(),
                message="Title is not matching. Incorrect text."
            )
            allure.attach(gecko_driver.title, "Page Title", allure.attachment_type.TEXT)

    @allure.story("URL Verification")
    @allure.title("Verify Main Page URL is Correct")
    def test_main_page_url(self, gecko_driver, wait_for):
        main_page = page.MainPage(gecko_driver)
        with allure.step("Verify the current URL matches expected"):
            wait_for(
                lambda: main_page.is_url_matches(),
                message="URL is incorrect after navigating to the Main Page!"
            )
            allure.attach(chrome_driver.current_url, "Current URL", allure.attachment_type.TEXT)

    @allure.story("Header Verification")
    @allure.title("Verify Main Page Header Matches Expected Text")
    def test_main_page_header(self, chrome_driver, wait_for):
        main_page = page.MainPage(chrome_driver)
        with allure.step("Verify main header text"):
            wait_for(
                lambda: main_page.is_main_header_matches(),
                message="Main Header is not matching. Incorrect text."
            )
            allure.attach(main_page.get_main_header_text(), "Main Header", allure.attachment_type.TEXT)

    @pytest.mark.parametrize("button_method, description", [
        ("click_navigation_button_main", "Main"),
        ("click_navigation_button_nums", "Random Numbers"),
        ("click_navigation_button_caesar", "Caesar"),
        ("click_navigation_button_vigenere", "Vigenere"),
        ("click_navigation_button_colyte", "Colyte"),
    ])
    @allure.story("Navigation Buttons")
    @allure.title("Verify navigation button redirects to correct page")
    def test_navigation_buttons(self, gecko_driver, wait_for, button_method, description):
        main_page = page.MainPage(gecko_driver)
        with allure.step(f"Click navigation button: {description}"):
            action = getattr(main_page, button_method)
            wait_for(
                lambda: action(),
                message=f"URL is incorrect after clicking on navigation button '{description}'."
            )
            allure.attach(gecko_driver.current_url, "Redirected URL", allure.attachment_type.TEXT)
