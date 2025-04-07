from time import sleep
from selenium.webdriver.common.by import By
from locators import *

main_url = "https://stellarburgers.nomoreparties.site"
endpoint_url = "/register"

def test_registration_correct(driver, create_login, create_password):
    driver.get(main_url + endpoint_url)
    driver.find_element(By.XPATH, RegistrationPageLocators.name_field).send_keys("test_name")
    driver.find_element(By.XPATH, RegistrationPageLocators.email_field).send_keys(create_login)
    driver.find_element(By.XPATH, RegistrationPageLocators.password_field).send_keys(create_password)
    driver.find_element(By.XPATH, RegistrationPageLocators.register_button).click()
    driver.find_element(By.XPATH, LoginPageLocators.login_form).is_displayed()
    sleep(0.5)
    assert '/login' in driver.current_url

def test_registration_without_name(driver, create_login, create_password):
    driver.get(main_url + endpoint_url)
    driver.find_element(By.XPATH, RegistrationPageLocators.email_field).send_keys(create_login)
    driver.find_element(By.XPATH, RegistrationPageLocators.password_field).send_keys(create_password)
    driver.find_element(By.XPATH, RegistrationPageLocators.register_button).click()
    sleep(0.5)
    assert '/register' in driver.current_url

def test_registration_short_password(driver, create_login, create_password):
    driver.get(main_url + endpoint_url)
    driver.find_element(By.XPATH, RegistrationPageLocators.email_field).send_keys(create_login)
    driver.find_element(By.XPATH, RegistrationPageLocators.password_field).send_keys(create_password[1:])
    driver.find_element(By.XPATH, RegistrationPageLocators.register_button).click()
    assert driver.find_element(By.XPATH, RegistrationPageLocators.error_message).is_displayed()