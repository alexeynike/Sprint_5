class RegistrationPageLocators:
    name_field = "//label[text()='Имя']/../input"
    email_field = "//label[text()='Email']/../input"
    password_field = "//input[@type='password']"
    register_button = "//button[contains(@class, 'button_type_primary')]"
    error_message = "//p[contains(@class, 'input__error')]"
    login_link = "//a[contains(@class, 'Auth_link')]"

class LoginPageLocators:
    login_form = "//h2[text()='Вход']/.."
    login_btn = "//button[contains(@class, 'button_button')]"

class HomePageLocators:
    login_btn = "//button[contains(@class, 'button_button')]"
    order_btn = "//button[contains(@class, 'button_button')]"
    profile_link = "// p[text() = 'Личный Кабинет'] /.."
    bread_tab = "//span[text()='Булки']/.."
    sauce_tab = "//span[text()='Соусы']/.."
    ingredients_tab = "//span[text()='Начинки']/.."

class RestorePageLocators:
    login_link = "//a[contains(@class, 'Auth_link')]"

class ProfilePageLocators:
    logout_btn = "//button[contains(@class, 'Account_button')]"

