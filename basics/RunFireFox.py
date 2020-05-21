from selenium import webdriver


class RunFireFox:
    def test(self):
        driver = webdriver.Firefox(
            executable_path='/Users/sdhole/Documents/python_workspace/SeleniumWithPython/libs/geckodriver')
        driver.get("https://www.youtube.com")


ff = RunFireFox()
ff.test()
