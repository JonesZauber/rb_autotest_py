import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.home
def test_load_home_page(open_home_page):
    driver = open_home_page
    current_url = driver.current_url
    assert current_url == "https://www.redbull.com/at-de/"


@pytest.mark.home
def test_load_home_page_by_press_main_logo(open_home_page):
    driver = open_home_page
    main_logo = driver.find_element(By.CLASS_NAME, 'menu-header__logo')
    driver.implicitly_wait(5)
    main_logo.click()
    current_url = driver.current_url
    assert current_url == "https://www.redbull.com/at-de/"


@pytest.mark.home
def test_main_page_title(open_home_page):
    driver = open_home_page
    driver.implicitly_wait(5)
    title = driver.title
    assert title == 'Red Bull verleiht Flügel - RedBull.com'


@pytest.mark.home
def test_accept_cookies():
    driver = webdriver.Chrome()
    driver.get("https://www.redbull.com/")
    driver.implicitly_wait(5)
    cookies_before = driver.get_cookies()
    found_before = any(d.get('name') == 'OptanonAlertBoxClosed' for d in cookies_before)
    assert found_before == False
    cookie_accept = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
    cookie_accept.click()
    cookies_after = driver.get_cookies()
    found_after = any(d.get('name') == 'OptanonAlertBoxClosed' for d in cookies_after)
    assert found_after == True


@pytest.mark.home
def test_back_to_home_page(open_home_page):
    driver = open_home_page
    header_navigation = ['events', 'athletes', 'energydrink']
    for item in header_navigation:
        url = 'https://www.redbull.com/at-de/' + item
        driver.get(url)
        main_logo = driver.find_element(By.CSS_SELECTOR, '[alt="Red Bull Logo"]')
        main_logo.click()
        current_url = driver.current_url
        assert current_url == "https://www.redbull.com/at-de/"


@pytest.mark.home
def test_back_to_home_page_from_live(open_home_page):
    driver = open_home_page
    driver.get("https://www.redbull.com/at-de/live-events")
    hover_element = driver.find_element(By.CSS_SELECTOR, '#page-main button.global-header__content')
    hover_element.click()
    main_logo = driver.find_element(By.CSS_SELECTOR, '[alt="Red Bull Logo"]')
    main_logo.click()
    current_url = driver.current_url
    assert current_url == "https://www.redbull.com/at-de/"







