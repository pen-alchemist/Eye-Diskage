from functional_tests.pages import main_page_object as page


def test_main_page_title(chrome_driver, wait_for):
    """Test that Main Page title is correct."""
    main_page = page.MainPage(chrome_driver)
    wait_for(main_page.is_title_matches())


def test_main_page_url(chrome_driver, wait_for):
    """Test that URL is correct after opening Main Page."""
    main_page = page.MainPage(chrome_driver)
    wait_for(main_page.is_url_matches())


def test_main_page_header(chrome_driver, wait_for):
    """Test that Main Page main header is correct."""
    main_page = page.MainPage(chrome_driver)
    wait_for(lambda: main_page.is_main_header_matches())

def test_navigate_button_click(chrome_driver, wait_for):
    """Test that URL is correct after clicking on navigation button."""
    main_page = page.MainPage(chrome_driver)
    wait_for(main_page.click_navigation_button())


def test_main_page_sub_header(chrome_driver, wait_for):
    """Test that Main Page sub header is correct."""
    main_page = page.MainPage(chrome_driver)
    wait_for(main_page.is_sub_header_matches())


def test_main_page_no_posts_message(chrome_driver, wait_for):
    """Test that Main Page no posts message text is correct."""
    main_page = page.MainPage(chrome_driver)
    wait_for(main_page.is_no_posts_message_matches())


def test_main_pages_counter(chrome_driver, wait_for):
    """Test that Main Page pages counter text is correct."""
    main_page = page.MainPage(chrome_driver)
    wait_for(main_page.is_pages_counter_matches())


def test_previous_button_disabled(chrome_driver, wait_for):
    """Test that previous button is disabled on Main Page."""
    main_page = page.MainPage(chrome_driver)
    wait_for(main_page.disabled_page_previous_button())


def test_next_button_disabled(chrome_driver, wait_for):
    """Test that next button is disabled on Main Page."""
    main_page = page.MainPage(chrome_driver)
    wait_for(main_page.disabled_page_next_button())


def test_footer_text(chrome_driver, wait_for):
    """Test that footer text is correct."""
    main_page = page.MainPage(chrome_driver)
    wait_for(main_page.is_footer_matches())
