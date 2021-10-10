import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as u1
import allure
import moment

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')

        login = LoginPage(driver)
        login.enter_username(u1.USERNAME)
        login.enter_password(u1.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "abc"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            screenshotName = "error1_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(),name="error1",attachment_type=allure.attachment_type.PNG)
            raise

        except:
            print("There was an exception")
            raise

        else:
            print("No exceptions occurred")

        finally:
            print("I am inside finally block")

        #driver.find_element_by_id("welcome").click()
        #driver.find_element_by_link_text("Logout").click()












