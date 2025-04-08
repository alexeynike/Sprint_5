from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import *
from test_data import *

class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.get(main_url)
        driver.find_element(By.XPATH, HomePageLocators.LOGIN_BTN).click()
        driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_FIELD).send_keys(login)
        driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BTN).click()
        assert driver.find_element(By.XPATH, HomePageLocators.ORDER_BTN).is_displayed()

    def test_login_from_profile_page(self, driver):
        driver.get(main_url)
        driver.find_element(By.XPATH, HomePageLocators.PROFILE_LINK).click()
        driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_FIELD).send_keys(login)
        driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BTN).click()
        assert driver.find_element(By.XPATH, HomePageLocators.ORDER_BTN).is_displayed()

    def test_login_from_registration_page(self, driver):
        driver.get(main_url + '/register')
        driver.find_element(By.XPATH, RegistrationPageLocators.LOGIN_LINK).click()
        driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_FIELD).send_keys(login)
        driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BTN).click()
        assert driver.find_element(By.XPATH, HomePageLocators.ORDER_BTN).is_displayed()

    def test_login_from_restore_page(self, driver):
        driver.get(main_url + '/forgot-password')
        driver.find_element(By.XPATH, RestorePageLocators.LOGIN_LINK).click()
        driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_FIELD).send_keys(login)
        driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BTN).click()
        assert driver.find_element(By.XPATH, HomePageLocators.ORDER_BTN).is_displayed()

    def test_open_profile_page(self, driver):
        driver.get(main_url)
        driver.find_element(By.XPATH, HomePageLocators.LOGIN_BTN).click()
        driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_FIELD).send_keys(login)
        driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BTN).click()
        driver.find_element(By.XPATH, HomePageLocators.PROFILE_LINK).click()
        assert WebDriverWait(driver, 3).until(EC.url_contains('/account/profile'))

    def test_exit_from_login_page(self, driver):
        driver.get(main_url)
        driver.find_element(By.XPATH, HomePageLocators.LOGIN_BTN).click()
        driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_FIELD).send_keys(login)
        driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BTN).click()
        driver.find_element(By.XPATH, HomePageLocators.PROFILE_LINK).click()
        driver.find_element(By.XPATH, ProfilePageLocators.LOGOUT_BTN).click()
        assert WebDriverWait(driver, 3).until(EC.url_contains('/login'))

    def test_constructor_tab_default_active(self, driver):
        driver.get(main_url)
        active_tab = driver.find_element(By.XPATH, HomePageLocators.BREAD_TAB)
        assert active_class in active_tab.get_attribute('class').split()

    def test_move_to_sauce_tab(self, driver):
        driver.get(main_url)
        sauce_tab = driver.find_element(By.XPATH, HomePageLocators.SAUCE_TAB)
        sauce_tab.click()
        assert active_class in sauce_tab.get_attribute('class').split()

    def test_move_to_ingredients_tab(self, driver):
        driver.get(main_url)
        ingredients_tab = driver.find_element(By.XPATH, HomePageLocators.INGREDIENTS_TAB)
        ingredients_tab.click()
        assert active_class in ingredients_tab.get_attribute('class').split()

    def test_move_from_ingredients_tab(self, driver):
        driver.get(main_url)
        driver.find_element(By.XPATH, HomePageLocators.INGREDIENTS_TAB).click()
        bread_tab = driver.find_element(By.XPATH, HomePageLocators.BREAD_TAB)
        bread_tab.click()
        assert active_class in bread_tab.get_attribute('class').split()
