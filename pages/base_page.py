from selenium.common.exceptions import *


class BasePage(BaseException):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except 'BaseException':
            return False
        return True

# if __name__ == "__main__":
#     open()
