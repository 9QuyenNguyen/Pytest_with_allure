import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure
from allure_commons.types import AttachmentType


@pytest.fixture()
def chrome_browser():
    # driver = webdriver.Chrome()

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.implicitly_wait(10)
    # Yield the WebDriver instance
    yield driver
    # Close the WebDriver instance
    driver.quit()

def test_title(chrome_browser):
    """
    Test the title of the https://tiki.vn/ website
    """
    chrome_browser.get("https://tiki.vn/")
    assert chrome_browser.title == "Tiki - Mua hàng online giá tốt, hàng chuẩn, ship nhanh"


def test_search(chrome_browser):
    """
    Test the search functionality of the Tiki website
    """
    url = "https://tiki.vn/"
    search_term = "iphone 13"
    # Navigate to the Google home page.
    chrome_browser.get(url)

    # Find the search box using its name attribute value.
    search_box = chrome_browser.find_element(By.XPATH, value="//input[@placeholder='Bạn tìm gì hôm nay']")

    # Enter a search query and submit.
    search_box.send_keys(search_term + Keys.RETURN)

    content_value = search_box.get_attribute("value")
    allure.attach(chrome_browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    # Assert that the title contains the search term.
    assert content_value == search_term


