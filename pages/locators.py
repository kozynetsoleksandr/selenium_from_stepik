from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")  # Кортеж


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_USER_NAME = (By.ID, 'id_login-username')
    LOGIN_USER_PASSWORD = (By.ID, 'id_login-password')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_USER_NAME = (By.ID, 'id_registration-email')
    REGISTER_USER_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTER_USER_PASSWORD_CONFIRM = (By.ID, 'id_registration-password2')
