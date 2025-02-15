from functional_tests.pages import main_page_object as page


def test_main_page_title(gecko_driver, wait_for):
    """Test that Main Page title is correct."""
    main_page = page.MainPage(gecko_driver)
    wait_for(
        lambda: main_page.is_title_matches(),
        message="Title is not matching. Incorrect text."
    )


def test_main_page_url(gecko_driver, wait_for):
    """Test that URL is correct after opening Main Page."""
    main_page = page.MainPage(gecko_driver)
    wait_for(
        lambda: main_page.is_url_matches(),
        message="URL is incorrect after navigating to the Main Page!"
    )


def test_main_page_header(gecko_driver, wait_for):
    """Test that the Main Page main header matches the expected value."""
    main_page = page.MainPage(gecko_driver)
    wait_for(
        lambda: main_page.is_main_header_matches(),
        message="Main Header is not matching. Incorrect text."
    )


def test_navigate_button_main_click(gecko_driver, wait_for):
    """Test that URL is correct after clicking on navigation button."""
    main_page = page.MainPage(gecko_driver)
    wait_for(
        lambda: main_page.click_navigation_button_main(),
        message="URL is incorrect after clicking on navigation button 'Main'."
    )


def test_navigate_button_nums_click(gecko_driver, wait_for):
    """Test that URL is correct after clicking on navigation button."""
    main_page = page.MainPage(gecko_driver)
    wait_for(
        lambda: main_page.click_navigation_button_nums(),
        message="URL is incorrect after clicking on navigation button 'Random Numbers'."
    )


def test_navigate_button_caesar_click(gecko_driver, wait_for):
    """Test that URL is correct after clicking on navigation button."""
    main_page = page.MainPage(gecko_driver)
    wait_for(
        lambda: main_page.click_navigation_button_caesar(),
        message="URL is incorrect after clicking on navigation button 'Caesar'."
    )


def test_navigate_button_vigenere_click(gecko_driver, wait_for):
    """Test that URL is correct after clicking on navigation button."""
    main_page = page.MainPage(gecko_driver)
    wait_for(
        lambda: main_page.click_navigation_button_vigenere(),
        message="URL is incorrect after clicking on navigation button 'Vigenere'."
    )


def test_navigate_button_colyte_click(gecko_driver, wait_for):
    """Test that URL is correct after clicking on navigation button."""
    main_page = page.MainPage(gecko_driver)
    wait_for(
        lambda: main_page.click_navigation_button_colyte(),
        message="URL is incorrect after clicking on navigation button 'Colyte'."
    )
