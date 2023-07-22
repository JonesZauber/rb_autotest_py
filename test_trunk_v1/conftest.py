from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def open_home_page():
    # Create a WebDriver instance for Chrome
    browser = webdriver.Chrome()
    # Preconditions
    browser.maximize_window()
    browser.get("https://www.redbull.com/")
    browser.implicitly_wait(5)
    # Accept cookies
    cookie = browser.find_element(By.ID, 'onetrust-accept-btn-handler')
    cookie.click()
    # Return the WebDriver instance to make it available to the tests
    return browser


@pytest.fixture()
def enter_profile(open_home_page):
    driver = open_home_page
    # Press login icon
    login_icon = driver.find_element(By.XPATH, '//button[@class="user-icon"]')
    login_icon.click()
    driver.implicitly_wait(5)
    # Enter user email
    email_input = driver.find_element(By.ID, 'email')
    email_input.click()
    email_input.send_keys("joneszauber@gmail.com")
    driver.implicitly_wait(5)
    # Press submit button
    submit_email_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_email_button.click()
    # Enter user password
    pass_input = driver.find_element(By.ID, 'lb-password')
    pass_input.click()
    pass_input.send_keys("testing")
    driver.implicitly_wait(5)
    # Press submit button
    submit_button = driver.find_element(By.XPATH, '//input[@id="lb-password"]/following::button[@type="submit"]')
    submit_button.click()
    driver.implicitly_wait(5)
    return driver
