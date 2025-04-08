from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import *
from test_data import *

class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.get(main_url)
        driver.find_element(By.XPATH, HomePageLocators.login_btn).click()
        driver.find_element(By.XPATH, RegistrationPageLocators.email_field).send_keys(login)
        driver.find_element(By.XPATH, RegistrationPageLocators.password_field).send_keys(password)
        driver.find_element(By.XPATH, LoginPageLocators.login_btn).click()
        assert driver.find_element(By.XPATH, HomePageLocators.order_btn).is_displayed()

    def test_login_from_profile_page(self, driver):
        driver.get(main_url)
        driver.find_element(By.XPATH, HomePageLocators.profile_link).click()
        driver.find_element(By.XPATH, RegistrationPageLocators.email_field).send_keys(login)
        driver.find_element(By.XPATH, RegistrationPageLocators.password_field).send_keys(password)
        driver.find_element(By.XPATH, LoginPageLocators.login_btn).click()
        assert driver.find_element(By.XPATH, HomePageLocators.order_btn).is_displayed()

    def test_login_from_registration_page(self, driver):
        driver.get(main_url + '/register')
        driver.find_element(By.XPATH, RegistrationPageLocators.login_link).click()
        driver.find_element(By.XPATH, RegistrationPageLocators.email_field).send_keys(login)
        driver.find_element(By.XPATH, RegistrationPageLocators.password_field).send_keys(password)
        driver.find_element(By.XPATH, LoginPageLocators.login_btn).click()
        assert driver.find_element(By.XPATH, HomePageLocators.order_btn).is_displayed()

    def test_login_from_restore_page(self, driver):
        driver.get(main_url + '/forgot-password')
        driver.find_element(By.XPATH, RestorePageLocators.login_link).click()
        driver.find_element(By.XPATH, RegistrationPageLocators.email_field).send_keys(login)
        driver.find_element(By.XPATH, RegistrationPageLocators.password_field).send_keys(password)
        driver.find_element(By.XPATH, LoginPageLocators.login_btn).click()
        assert driver.find_element(By.XPATH, HomePageLocators.order_btn).is_displayed()

    def test_open_profile_page(self, driver):
        driver.get(main_url)
        driver.find_element(By.XPATH, HomePageLocators.login_btn).click()
        driver.find_element(By.XPATH, RegistrationPageLocators.email_field).send_keys(login)
        driver.find_element(By.XPATH, RegistrationPageLocators.password_field).send_keys(password)
        driver.find_element(By.XPATH, LoginPageLocators.login_btn).click()
        driver.find_element(By.XPATH, HomePageLocators.profile_link).click()
        assert WebDriverWait(driver, 3).until(EC.url_contains('/account/profile'))


    def test_exit_from_login_page(self, driver):
        driver.get(main_url)
        driver.find_element(By.XPATH, HomePageLocators.login_btn).click()
        driver.find_element(By.XPATH, RegistrationPageLocators.email_field).send_keys(login)
        driver.find_element(By.XPATH, RegistrationPageLocators.password_field).send_keys(password)
        driver.find_element(By.XPATH, LoginPageLocators.login_btn).click()
        driver.find_element(By.XPATH, HomePageLocators.profile_link).click()
        driver.find_element(By.XPATH, ProfilePageLocators.logout_btn).click()
        assert WebDriverWait(driver, 3).until(EC.url_contains('/login'))

    def test_constructor_tab_default_active(self, driver):
        driver.get(main_url)
        active_tab = driver.find_element(By.XPATH, HomePageLocators.bread_tab)
        assert active_class in active_tab.get_attribute('class').split()

    def test_move_to_sauce_tab(self, driver):
        driver.get(main_url)
        sauce_tab = driver.find_element(By.XPATH, HomePageLocators.sauce_tab)
        sauce_tab.click()
        assert active_class in sauce_tab.get_attribute('class').split()

    def test_move_to_ingredients_tab(self, driver):
        driver.get(main_url)
        ingredients_tab = driver.find_element(By.XPATH, HomePageLocators.ingredients_tab)
        ingredients_tab.click()
        assert active_class in ingredients_tab.get_attribute('class').split()

    def test_move_from_ingredients_tab(self, driver):
        driver.get(main_url)
        driver.find_element(By.XPATH, HomePageLocators.ingredients_tab).click()
        bread_tab = driver.find_element(By.XPATH, HomePageLocators.bread_tab)
        bread_tab.click()
        assert active_class in bread_tab.get_attribute('class').split()

