from functional_tests.pages import main_page_object as page


def test_main_page_title(chrome_driver, wait_for):
    """Test that Main Page title is correct."""
    main_page = page.MainPage(chrome_driver)
    wait_for(lambda: main_page.is_title_matches())
    assert main_page.is_title_matches()


def test_main_page_url(chrome_driver, wait_for):
    """Test that URL is correct after opening Main Page."""
    main_page = page.MainPage(chrome_driver)
    wait_for(lambda: main_page.is_url_matches())
    assert main_page.is_url_matches()


def test_main_page_header(chrome_driver, wait_for):
    """Test that the Main Page main header matches the expected value."""
    main_page = page.MainPage(chrome_driver)
    wait_for(lambda: main_page.is_main_header_matches())
    assert main_page.is_main_header_matches()


def test_navigate_button_main_click(chrome_driver, wait_for):
    """Test that URL is correct after clicking on navigation button."""
    main_page = page.MainPage(chrome_driver)
    wait_for(lambda: main_page.click_navigation_button_main())
    assert main_page.click_navigation_button_main()


def test_navigate_button_nums_click(chrome_driver, wait_for):
    """Test that URL is correct after clicking on navigation button."""
    main_page = page.MainPage(chrome_driver)
    wait_for(lambda: main_page.click_navigation_button_nums())
    assert main_page.click_navigation_button_nums()


def test_navigate_button_caesar_click(chrome_driver, wait_for):
    """Test that URL is correct after clicking on navigation button."""
    main_page = page.MainPage(chrome_driver)
    wait_for(lambda: main_page.click_navigation_button_caesar())
    assert main_page.click_navigation_button_caesar()


def test_navigate_button_vigenere_click(chrome_driver, wait_for):
    """Test that URL is correct after clicking on navigation button."""
    main_page = page.MainPage(chrome_driver)
    wait_for(lambda: main_page.click_navigation_button_vigenere())
    assert main_page.click_navigation_button_vigenere()


def test_navigate_button_colyte_click(chrome_driver, wait_for):
    """Test that URL is correct after clicking on navigation button."""
    main_page = page.MainPage(chrome_driver)
    wait_for(lambda: main_page.click_navigation_button_colyte())
    assert main_page.click_navigation_button_colyte()


def test_main_page_sub_header(chrome_driver, wait_for):
    """Test that Main Page sub header is correct."""
    main_page = page.MainPage(chrome_driver)
    wait_for(lambda: main_page.is_sub_header_matches())
    assert main_page.is_sub_header_matches()

def test_footer_text(chrome_driver, wait_for):
    """Test that footer text is correct."""
    main_page = page.MainPage(chrome_driver)
    wait_for(lambda: main_page.is_footer_matches())
    assert main_page.is_main_header_matches()
