from time import sleep
from selenium.webdriver.common.by import By
from locators import *

main_url = "https://stellarburgers.nomoreparties.site"
login = "test12345@gmail.com"
password = "test1234qwerty123"
active_class = "tab_tab_type_current__2BEPc"

def test_login_from_main_page(driver):
    driver.get(main_url)
    driver.find_element(By.XPATH, HomePageLocators.login_btn).click()
    driver.find_element(By.XPATH, RegistrationPageLocators.email_field).send_keys(login)
    driver.find_element(By.XPATH, RegistrationPageLocators.password_field).send_keys(password)
    driver.find_element(By.XPATH, LoginPageLocators.login_btn).click()
    driver.find_element(By.XPATH, HomePageLocators.order_btn).is_displayed()

def test_login_from_profile_page(driver):
    driver.get(main_url)
    driver.find_element(By.XPATH, HomePageLocators.profile_link).click()
    driver.find_element(By.XPATH, RegistrationPageLocators.email_field).send_keys(login)
    driver.find_element(By.XPATH, RegistrationPageLocators.password_field).send_keys(password)
    driver.find_element(By.XPATH, LoginPageLocators.login_btn).click()
    driver.find_element(By.XPATH, HomePageLocators.order_btn).is_displayed()

def test_login_from_registration_page(driver):
    driver.get(main_url + '/register')
    driver.find_element(By.XPATH, RegistrationPageLocators.login_link).click()
    driver.find_element(By.XPATH, RegistrationPageLocators.email_field).send_keys(login)
    driver.find_element(By.XPATH, RegistrationPageLocators.password_field).send_keys(password)
    driver.find_element(By.XPATH, LoginPageLocators.login_btn).click()
    driver.find_element(By.XPATH, HomePageLocators.order_btn).is_displayed()

def test_login_from_restore_page(driver):
    driver.get(main_url + '/forgot-password')
    driver.find_element(By.XPATH, RestorePageLocators.login_link).click()
    driver.find_element(By.XPATH, RegistrationPageLocators.email_field).send_keys(login)
    driver.find_element(By.XPATH, RegistrationPageLocators.password_field).send_keys(password)
    driver.find_element(By.XPATH, LoginPageLocators.login_btn).click()
    driver.find_element(By.XPATH, HomePageLocators.order_btn).is_displayed()

def test_open_profile_page(driver):
    driver.get(main_url)
    driver.find_element(By.XPATH, HomePageLocators.login_btn).click()
    driver.find_element(By.XPATH, RegistrationPageLocators.email_field).send_keys(login)
    driver.find_element(By.XPATH, RegistrationPageLocators.password_field).send_keys(password)
    driver.find_element(By.XPATH, LoginPageLocators.login_btn).click()
    driver.find_element(By.XPATH, HomePageLocators.profile_link).click()
    sleep(1)
    assert '/account/profile' in driver.current_url


def test_exit_from_login_page(driver):
    driver.get(main_url)
    driver.find_element(By.XPATH, HomePageLocators.login_btn).click()
    driver.find_element(By.XPATH, RegistrationPageLocators.email_field).send_keys(login)
    driver.find_element(By.XPATH, RegistrationPageLocators.password_field).send_keys(password)
    driver.find_element(By.XPATH, LoginPageLocators.login_btn).click()
    driver.find_element(By.XPATH, HomePageLocators.profile_link).click()
    driver.find_element(By.XPATH, ProfilePageLocators.logout_btn).click()
    sleep(1)
    assert '/login' in driver.current_url

def test_constructor_tab_default_active(driver):
    driver.get(main_url)
    active_tab = driver.find_element(By.XPATH, HomePageLocators.bread_tab)
    assert active_class in active_tab.get_attribute('class').split()

def test_move_to_sauce_tab(driver):
    driver.get(main_url)
    sauce_tab = driver.find_element(By.XPATH, HomePageLocators.sauce_tab)
    sauce_tab.click()
    assert active_class in sauce_tab.get_attribute('class').split()

def test_move_to_ingredients_tab(driver):
    driver.get(main_url)
    ingredients_tab = driver.find_element(By.XPATH, HomePageLocators.ingredients_tab)
    ingredients_tab.click()
    assert active_class in ingredients_tab.get_attribute('class').split()

def test_move_from_ingredients_tab(driver):
    driver.get(main_url)
    driver.find_element(By.XPATH, HomePageLocators.ingredients_tab).click()
    bread_tab = driver.find_element(By.XPATH, HomePageLocators.bread_tab)
    bread_tab.click()
    assert active_class in bread_tab.get_attribute('class').split()

