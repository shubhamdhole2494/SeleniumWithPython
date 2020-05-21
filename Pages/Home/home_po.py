from selenium.webdriver.common.by import By
from Base.Selenium_Driver import SeleniumDriver


class HomePageObject(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _signIn_button = "login"

    # Get Element
    def getsignInButton(self):
        return self.getElement(self._signIn_button, "classname")
        # return self.driver.find_element(By.CLASS_NAME, self._signIn_button)

    # Perform Action on element
    def clickOnsignInButton(self):
        self.getsignInButton().click()
