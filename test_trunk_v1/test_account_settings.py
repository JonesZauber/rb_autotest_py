import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest


@pytest.mark.account
def test_enter_account_settings(enter_profile):
    driver = enter_profile
    account_icon = driver.find_element(By.XPATH, '//*[@id="page-main"]/div/div[3]/div/div/div/div/div/div[1]/div/div'
                                                 '/div/header/div[1]/div[2]/div[1]/div/button/div/div')
    account_icon.click()
    driver.implicitly_wait(5)
    settings_button = driver.find_element(By.XPATH, '//*[@id="page-main"]/div/div[3]/div/div/div/div/div/div[1]/div'
                                                    '/div/div/header/div[1]/div[2]/div[2]/div/div/div/div[2]/a[2]')
    settings_button.click()
    partial_url = 'https://www.redbull.com/account/profile/settings'
    assert partial_url in driver.current_url
    time.sleep(5)


@pytest.mark.account
def test_name_email_in_profile_serrings(enter_profile):
    driver = enter_profile
    account_icon = driver.find_element(By.XPATH, '//*[@id="page-main"]/div/div[3]/div/div/div/div/div/div[1]/div/div'
                                                 '/div/header/div[1]/div[2]/div[1]/div/button/div/div')
    account_icon.click()
    driver.implicitly_wait(5)
    settings_button = driver.find_element(By.XPATH, '//*[@id="page-main"]/div/div[3]/div/div/div/div/div/div[1]/div'
                                                    '/div/div/header/div[1]/div[2]/div[2]/div/div/div/div[2]/a[2]')
    settings_button.click()
    user_name = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]')
    assert user_name.text == 'Jones Zauber'
    user_mail = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]')
    assert user_mail.text == 'joneszauber@gmail.com'
    user_residence = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/span')
    assert user_residence.text == 'Austria' or 'Österreich'


@pytest.mark.account
def test_direct_marketing_consent(enter_profile):
    driver = enter_profile
    account_icon = driver.find_element(By.XPATH, '//*[@id="page-main"]/div/div[3]/div/div/div/div/div/div[1]/div/div'
                                                 '/div/header/div[1]/div[2]/div[1]/div/button/div/div')
    account_icon.click()
    driver.implicitly_wait(5)
    settings_button = driver.find_element(By.XPATH, '//*[@id="page-main"]/div/div[3]/div/div/div/div/div/div[1]/div'
                                                    '/div/div/header/div[1]/div[2]/div[2]/div/div/div/div[2]/a[2]')
    settings_button.click()
    mark_cons = driver.find_elements(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div[5]/'
                                                              'div[2]/label/span')
    direct_marketing_consent = ''
    accpectet_direct_marketing_consent = '''
    Ja! Red Bull GmbH, Österreich, kann die von mir zur Verfügung gestellten personenbezogenen Daten (d.h. Name,
    E-Mail-Adresse und meine Interessen) verarbeiten, um mich über relevante Veranstaltungen, Produkte & Aktivierungen
    aus der World of Red Bull per E-Mail und andere elektronische Kommunikationsmittel zu informieren. Ich kann mich
    jederzeit abmelden, indem ich auf Abmelden klicke oder die Einstellungen in meinem Red Bull Account-Profil ändere.
    Weitere Informationen findest du in der Datenschutzrichtlinie.
    '''.replace('\n', '').replace('    ', '').split('\n')
    for text_block in mark_cons:
        direct_marketing_consent += text_block.text
    assert direct_marketing_consent == ' '.join(accpectet_direct_marketing_consent)


@pytest.mark.account
def test_checkbox_direct_marketing_consent(enter_profile):
    driver = enter_profile
    account_icon = driver.find_element(By.XPATH, '//*[@id="page-main"]/div/div[3]/div/div/div/div/div/div[1]/div/div'
                                                 '/div/header/div[1]/div[2]/div[1]/div/button/div/div')
    account_icon.click()
    driver.implicitly_wait(5)
    settings_button = driver.find_element(By.XPATH, '//*[@id="page-main"]/div/div[3]/div/div/div/div/div/div[1]/div'
                                                    '/div/div/header/div[1]/div[2]/div[2]/div/div/div/div[2]/a[2]')
    settings_button.click()
    checkbox = driver.find_element(By.XPATH, '//*[@id="https://policies.redbull.com/policies/RedBull.com_Austria/202112231437/de/privacy.html"]')
    assert not checkbox.is_selected()
    driver.implicitly_wait(5)

    checkbox = driver.find_element(By.XPATH, '//*[@id="https://policies.redbull.com/policies/RedBull.com_Austria/202112231437/de/privacy.html"]')
    checkbox.click()
    driver.implicitly_wait(5)
    time.sleep(5)
    assert checkbox.is_selected()


@pytest.mark.account
def test_world_of_redbull_link(enter_profile):
    driver = enter_profile
    account_icon = driver.find_element(By.XPATH, '//*[@id="page-main"]/div/div[3]/div/div/div/div/div/div[1]/div/div'
                                                 '/div/header/div[1]/div[2]/div[1]/div/button/div/div')
    account_icon.click()
    driver.implicitly_wait(5)
    settings_button = driver.find_element(By.XPATH, '//*[@id="page-main"]/div/div[3]/div/div/div/div/div/div[1]/div'
                                                    '/div/div/header/div[1]/div[2]/div[2]/div/div/div/div[2]/a[2]')
    settings_button.click()
    world_of_redbull = driver.find_element(By.LINK_TEXT, 'World of Red Bull')
    world_of_redbull.click()
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(5)
    time.sleep(5)
    assert driver.current_url == 'https://policies.redbull.com/policies/partners/202304141032/en/affiliates.html'


@pytest.mark.account
def test_privacy_policy_link(enter_profile):
    driver = enter_profile
    account_icon = driver.find_element(By.XPATH, '//*[@id="page-main"]/div/div[3]/div/div/div/div/div/div[1]/div/div'
                                                 '/div/header/div[1]/div[2]/div[1]/div/button/div/div')
    account_icon.click()
    driver.implicitly_wait(5)
    settings_button = driver.find_element(By.XPATH, '//*[@id="page-main"]/div/div[3]/div/div/div/div/div/div[1]/div'
                                                    '/div/div/header/div[1]/div[2]/div[2]/div/div/div/div[2]/a[2]')
    settings_button.click()
    privacy_policy = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div[5]/div[2]/label/span/a[2]')
    privacy_policy.click()
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(5)
    assert driver.current_url == 'https://policies.redbull.com/policies/RedBull.com_Austria/202112231437/de/privacy.html'


@pytest.mark.account
def test_residence_list(enter_profile):
    driver = enter_profile
    account_icon = driver.find_element(By.XPATH, '//*[@id="page-main"]/div/div[3]/div/div/div/div/div/div[1]/div/div'
                                                 '/div/header/div[1]/div[2]/div[1]/div/button/div/div')
    account_icon.click()
    driver.implicitly_wait(5)
    settings_button = driver.find_element(By.XPATH, '//*[@id="page-main"]/div/div[3]/div/div/div/div/div/div[1]/div'
                                                    '/div/div/header/div[1]/div[2]/div[2]/div/div/div/div[2]/a[2]')
    settings_button.click()
    edit = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div[4]/div[1]/span[2]')
    edit.click()

    dropdown = Select(driver.find_element(By.XPATH, '//*[@id="react-select-4-input"]'))
    options = [option.text for option in dropdown.options]

    print(options)

