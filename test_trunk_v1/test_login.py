import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.mark.login
def test_login_with_email(open_home_page):
    driver = open_home_page
    login_icon = driver.find_element(By.XPATH, '//button[@class="user-icon"]')
    login_icon.click()
    driver.implicitly_wait(5)
    email_input = driver.find_element(By.ID, 'email')
    email_input.click()
    email_input.send_keys("joneszauber@gmail.com")
    time.sleep(1)
    submit_email_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_email_button.click()
    pass_input = driver.find_element(By.ID, 'lb-password')
    pass_input.click()
    pass_input.send_keys("testing")
    time.sleep(1)
    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()
    time.sleep(5)


@pytest.mark.login
def test_login_with_gmail(open_home_page):
    driver = open_home_page
    login_icon = driver.find_element(By.XPATH, '//button[@class="user-icon"]')
    login_icon.click()
    driver.implicitly_wait(5)

    gmail_button = driver.find_element(By.XPATH, '//button[contains(@class, "google-btn")]')
    gmail_button.click()

    driver.switch_to.window(driver.window_handles[-1])
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId")))
    email_input.send_keys("joneszauber@gmail.com")
    email_input.send_keys(Keys.RETURN)

    password_input = WebDriverWait(driver, 10)\
        .until(EC.presence_of_element_located((By.XPATH, '//input[@name="Passwd"]')))
    password_input.send_keys("$Zauber17")
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)


@pytest.mark.login
def test_login_with_fb(open_home_page):
    driver = open_home_page
    login_icon = driver.find_element(By.XPATH, '//button[@class="user-icon"]')
    login_icon.click()
    driver.implicitly_wait(5)

    fb_button = driver.find_element(By.XPATH, '//button[contains(@class, "facebook-btn")]')
    fb_button.click()

    driver.switch_to.window(driver.window_handles[-1])
    fb_cookie = WebDriverWait(driver, 10)\
        .until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-cookiebanner="accept_button"]')))
    fb_cookie.click()

    driver.switch_to.window(driver.window_handles[-1])
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    email_input.send_keys("joneszauber@gmail.com")

    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'pass')))
    password_input.send_keys("$Zauber17")

    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'loginbutton')))
    password_input.send_keys(Keys.RETURN)

    time.sleep(3)


emails = ['test@test.co', 'test@test.com', 'test@test.comm']
@pytest.mark.login
@pytest.mark.parametrize('emails', emails)
def test_submit_email_button_enabled(open_home_page, emails):
    driver = open_home_page

    login_icon = driver.find_element(By.XPATH, '//button[@class="user-icon"]')
    login_icon.click()
    driver.implicitly_wait(5)

    email_input = driver.find_element(By.ID, 'email')
    email_input.click()
    email_input.clear()
    email_input.send_keys(emails)
    button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    assert button.is_enabled()


incorrect_emails = ['', 'test', 'test@', 'test@test', 'test@test.', 'test@test.c']
@pytest.mark.login
@pytest.mark.parametrize('incorrect_emails', incorrect_emails)
def test_submit_email_button_disabled(open_home_page, incorrect_emails):
    driver = open_home_page
    login_icon = driver.find_element(By.XPATH, '//button[@class="user-icon"]')
    login_icon.click()
    driver.implicitly_wait(5)

    email_input = driver.find_element(By.ID, 'email')
    email_input.click()
    email_input.clear()
    email_input.send_keys(incorrect_emails)
    button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    time.sleep(2)
    assert not button.is_enabled()


@pytest.mark.login
def test_submit_pass_button_disabled(open_home_page):
    driver = open_home_page
    login_icon = driver.find_element(By.XPATH, '//button[@class="user-icon"]')
    login_icon.click()
    driver.implicitly_wait(5)

    email_input = driver.find_element(By.ID, 'email')
    email_input.click()
    email_input.send_keys('joneszauber@gmail.com')
    time.sleep(1)

    submit_email_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_email_button.click()
    pass_input = driver.find_element(By.ID, 'lb-password')
    pass_input.click()
    button = driver.find_element(By.XPATH, '//button[@type="submit"]')

    passwords_list = ['a', 'b', 'c', 'd', 'e', 'd']
    password = []

    for letter in passwords_list:
        pass_input.send_keys(letter)
        password += letter
        if len(password) <= 4:
            assert not button.is_enabled()
        else:
            assert button.is_enabled()
