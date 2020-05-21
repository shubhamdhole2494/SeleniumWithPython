from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.Home.home_po import HomePageObject
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class registerTestCases(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePageObject(self.driver)

    def test_valid_reg(self):
        self.hp.clickOnsignInButton()

    def get_id(self):
        return 5


