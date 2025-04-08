import random
import string
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def create_login(length=15, domain="@ya.ru"):
    domain_length = len(domain)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length - domain_length)) + domain

@pytest.fixture(scope="function")
def create_password(length=6):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))