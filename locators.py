class RegistrationPageLocators:
    NAME_FIELD = "//label[text()='Имя']/../input"
    EMAIL_FIELD = "//label[text()='Email']/../input"
    PASSWORD_FIELD = "//input[@type='password']"
    REGISTER_BUTTON = "//button[contains(@class, 'button_type_primary')]"
    ERROR_MESSAGE = "//p[contains(@class, 'input__error')]"
    LOGIN_LINK = "//a[contains(@class, 'Auth_link')]"

class LoginPageLocators:
    LOGIN_FORM = "//h2[text()='Вход']/.."
    LOGIN_BTN = "//button[contains(@class, 'button_button')]"

class HomePageLocators:
    LOGIN_BTN = "//button[contains(@class, 'button_button')]"
    ORDER_BTN = "//button[contains(@class, 'button_button')]"
    PROFILE_LINK = "// p[text() = 'Личный Кабинет'] /.."
    BREAD_TAB = "//span[text()='Булки']/.."
    SAUCE_TAB = "//span[text()='Соусы']/.."
    INGREDIENTS_TAB = "//span[text()='Начинки']/.."

class RestorePageLocators:
    LOGIN_LINK = "//a[contains(@class, 'Auth_link')]"

class ProfilePageLocators:
    LOGOUT_BTN = "//button[contains(@class, 'Account_button')]"
