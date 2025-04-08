from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import *
from test_data import *


class TestRegistration:
    def test_registration_correct(self, driver, create_login, create_password):
        driver.get(main_url + endpoint_url)
        driver.find_element(By.XPATH, RegistrationPageLocators.NAME_FIELD).send_keys("test_name")
        driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_FIELD).send_keys(create_login)
        driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_FIELD).send_keys(create_password)
        driver.find_element(By.XPATH, RegistrationPageLocators.REGISTER_BUTTON).click()
        assert driver.find_element(By.XPATH, LoginPageLocators.LOGIN_FORM).is_displayed()
        assert WebDriverWait(driver, 3).until(EC.url_contains('/login'))

    def test_registration_without_name(self, driver, create_login, create_password):
        driver.get(main_url + endpoint_url)
        driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_FIELD).send_keys(create_login)
        driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_FIELD).send_keys(create_password)
        driver.find_element(By.XPATH, RegistrationPageLocators.REGISTER_BUTTON).click()
        assert WebDriverWait(driver, 3).until(EC.url_contains('/register'))

    def test_registration_short_password(self, driver, create_login, create_password):
        driver.get(main_url + endpoint_url)
        driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_FIELD).send_keys(create_login)
        driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_FIELD).send_keys(create_password[1:])
        driver.find_element(By.XPATH, RegistrationPageLocators.REGISTER_BUTTON).click()
        assert driver.find_element(By.XPATH, RegistrationPageLocators.ERROR_MESSAGE).is_displayed()
