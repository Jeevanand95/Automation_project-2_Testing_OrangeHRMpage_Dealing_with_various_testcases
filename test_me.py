#Guvi Project #2
#Name: R Jeevanand
# AT_9

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time


class Test_orangeHRmpage_testing:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    # Booting Method for running the Python Tests
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()

    def test_searchtextbox(self, booting_function):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
            "Admin")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
            "admin123")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(10)
        search_box = self.driver.find_element(by=By.XPATH,
                                              value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input")
        time.sleep(3)
        assert search_box.is_displayed() == True
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("Admin")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("pim")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("leave")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("time")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(
            "recruitment")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(
            "my info")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(
            "performance")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(
            "dashboard")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(
            "directory")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(
            "maintenance")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/form/div[3]/div/div[2]/input").send_keys(
            "admin123")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/form/div[4]/button[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("buzz")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("ADMIN")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("PIM")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("LEAVE")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("TIME")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(
            "RECRUITMENT")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(
            "MY INFO")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(
            "PERFORMANCE")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(
            "DASHBOARD")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(
            "DIRECTORY")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys(
            "MAINTENANCE")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/form/div[3]/div/div[2]/input").send_keys(
            "admin123")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/form/div[4]/button[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("BUZZ")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").click()
        time.sleep(3)

    def test_dropdown(self, booting_function):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
            "Admin")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
            "admin123")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/div/div/input").send_keys("Admin")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/i").click()
        time.sleep(3)
        dropdown_user_admin = self.driver.find_element(by=By.XPATH,
                                                       value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]")
        assert dropdown_user_admin.is_displayed() == True
        time.sleep(3)
        dropdown_user_ess = self.driver.find_element(by=By.XPATH,
                                                     value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]")
        assert dropdown_user_ess.is_displayed() == True
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(3)
        dropdown_status_enabled = self.driver.find_element(by=By.XPATH,
                                                           value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]")
        assert dropdown_status_enabled.is_displayed() == True
        time.sleep(3)
        dropdown_status_disabled = self.driver.find_element(by=By.XPATH,
                                                            value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[3]")
        assert dropdown_status_disabled.is_displayed() == True
        time.sleep(3)

    def test_PIM_employee(self, booting_function):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
            "Admin")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
            "admin123")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys(
            "Jeevanand")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys(
            "Raja")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").clear()
        time.sleep(3)
        act = ActionChains(self.driver)
        act.click(self.driver.find_element(by=By.XPATH,
                                           value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input")).key_down(
            Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").send_keys(
            "233")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys(
            "jeevanand")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys(
            "Rjeevanand@26")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys(
            "Rjeevanand@26")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(15)

    def test_employee_personaldetailsmenucheck(self, booting_function):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
            "Admin")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
            "admin123")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(
            "233")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div").click()
        time.sleep(3)
        personal_details = self.driver.find_element(by=By.XPATH,
                                                    value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a").is_displayed()
        assert personal_details == True
        time.sleep(3)
        contact_details = self.driver.find_element(by=By.XPATH,
                                                   value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a").is_displayed()
        assert contact_details == True
        time.sleep(3)
        emergency_contact = self.driver.find_element(by=By.XPATH,
                                                     value="//html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a").is_displayed()
        assert emergency_contact == True
        time.sleep(3)
        dependants = self.driver.find_element(by=By.XPATH,
                                              value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a").is_displayed()
        assert dependants == True
        time.sleep(3)
        job = self.driver.find_element(by=By.XPATH,
                                       value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a").is_displayed()
        assert job == True
        time.sleep(3)
        salary = self.driver.find_element(by=By.XPATH,
                                          value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a").is_displayed()
        assert salary == True
        time.sleep(3)
        tax_exemption = self.driver.find_element(by=By.XPATH,
                                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a").is_displayed()
        assert tax_exemption == True
        time.sleep(3)
        report_to = self.driver.find_element(by=By.XPATH,
                                             value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a").is_displayed()
        assert report_to == True
        time.sleep(3)
        qualification = self.driver.find_element(by=By.XPATH,
                                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]/a").is_displayed()
        assert qualification == True
        time.sleep(3)
        membership = self.driver.find_element(by=By.XPATH,
                                              value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[11]/a").is_displayed()
        assert membership == True
        time.sleep(3)

    def test_employee_personaldetails(self, booting_function):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
            "Admin")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
            "admin123")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(
            "233")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys(
            "jeeva")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input").send_keys(
            "AXXNUN2363")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input").send_keys(
            "2025-03-26")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input").send_keys(
            "25553636")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input").send_keys(
            "255537895")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[83]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input").send_keys(
            "1995-03-26")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label").click()

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input").send_keys(
            "No")

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click()

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[2]/i").click()

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div[2]/div[8]").click()

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button").click()

        time.sleep(15)
        employee_firstname = self.driver.find_element(by=By.XPATH,
                                                      value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").get_attribute(
            'value')

        assert employee_firstname == "Jeevanand"
        employee_lastname = self.driver.find_element(by=By.XPATH,
                                                     value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").get_attribute(
            'value')

        assert employee_lastname == "Raja"
        time.sleep(3)
        employee_nickname = self.driver.find_element(by=By.XPATH,
                                                     value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").get_attribute(
            'value')
        assert employee_nickname == "jeeva"
        time.sleep(3)
        employee_ID = self.driver.find_element(by=By.XPATH,
                                               value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input").get_attribute(
            'value')
        assert employee_ID == "233"
        time.sleep(3)
        employee_driverlicense = self.driver.find_element(by=By.XPATH,
                                                          value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input").get_attribute(
            'value')
        assert employee_driverlicense == "AXXNUN2363"
        time.sleep(3)
        employee_driverlicense_expiredate = self.driver.find_element(by=By.XPATH,
                                                                     value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input").get_attribute(
            'value')
        assert employee_driverlicense_expiredate == "2025-03-26"
        time.sleep(3)
        employee_ssnnumber = self.driver.find_element(by=By.XPATH,
                                                      value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input").get_attribute(
            'value')
        assert employee_ssnnumber == "25553636"
        time.sleep(3)
        employee_sinnumber = self.driver.find_element(by=By.XPATH,
                                                      value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input").get_attribute(
            'value')
        assert employee_sinnumber == "255537895"
        time.sleep(3)
        employee_sinnumber = self.driver.find_element(by=By.XPATH,
                                                      value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input").get_attribute(
            'value')
        assert employee_sinnumber == "255537895"
        time.sleep(3)
        employee_nationality = self.driver.find_element(by=By.XPATH,
                                                        value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]").get_attribute(
            "textContent")

        assert employee_nationality == "Indian"
        time.sleep(3)
        employee_martialstatus = self.driver.find_element(by=By.XPATH,
                                                          value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]").get_attribute(
            "textContent")

        assert employee_martialstatus == "Single"
        time.sleep(3)
        employee_DOB = self.driver.find_element(by=By.XPATH,
                                                value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input").get_attribute(
            'value')
        assert employee_DOB == "1995-03-26"
        time.sleep(3)
        employee_gender = self.driver.find_element(by=By.XPATH,
                                                   value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label").get_attribute(
            "textContent")
        assert employee_gender == "Male"
        time.sleep(3)
        employee_militaryservice = self.driver.find_element(by=By.XPATH,
                                                            value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input").get_attribute(
            'value')
        assert employee_militaryservice == "No"
        time.sleep(3)
        employee_Bloodtype = self.driver.find_element(by=By.XPATH,
                                                      value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div").get_attribute(
            "textContent")
        assert employee_Bloodtype == "AB+"
        time.sleep(3)

    def test_employee_contactdetails(self, booting_function):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
            "Admin")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
            "admin123")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(
            "233")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys(
            "NO.19B, wander street")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(
            "lal road, munipet, chennai-99")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input").send_keys(
            "chennai")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input").send_keys(
            "Tamil Nadu")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input").send_keys(
            "606009")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[100]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input").send_keys(
            "9956963214")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input").send_keys(
            "manier.1993.7@gmail.com")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button").click()
        time.sleep(15)

        employee_street1 = self.driver.find_element(by=By.XPATH,
                                                    value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").get_attribute(
            'value')

        assert employee_street1 == "NO.19B, wander street"
        employee_street2 = self.driver.find_element(by=By.XPATH,
                                                    value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").get_attribute(
            'value')

        assert employee_street2 == "lal road, munipet, chennai-99"
        time.sleep(3)
        employee_city = self.driver.find_element(by=By.XPATH,
                                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input").get_attribute(
            'value')
        assert employee_city == "chennai"
        time.sleep(3)
        employee_state = self.driver.find_element(by=By.XPATH,
                                                  value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input").get_attribute(
            'value')
        assert employee_state == "Tamil Nadu"
        time.sleep(3)
        employee_postalcode = self.driver.find_element(by=By.XPATH,
                                                       value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input").get_attribute(
            'value')
        assert employee_postalcode == "606009"
        time.sleep(3)
        employee_country = self.driver.find_element(by=By.XPATH,
                                                    value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]").get_attribute(
            'textContent')
        assert employee_country == "India"
        time.sleep(3)
        employee_mobile = self.driver.find_element(by=By.XPATH,
                                                   value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input").get_attribute(
            'value')
        assert employee_mobile == "9956963214"
        time.sleep(3)
        employee_mailid = self.driver.find_element(by=By.XPATH,
                                                   value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input").get_attribute(
            'value')
        assert employee_mailid == "manier.1993.7@gmail.com"
        time.sleep(3)

    def test_employee_emergencycontactdetails(self, booting_function):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
            "Admin")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
            "admin123")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(
            "233")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click()
        time.sleep(3)

        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Manikandan")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(
            "Brother")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input").send_keys(
            "9856932145")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]").click()
        time.sleep(15)
        emergency_contactname = self.driver.find_element(by=By.XPATH,
                                                         value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div").get_attribute(
            "textContent")
        assert emergency_contactname == "Manikandan"
        emergency_contactrelation = self.driver.find_element(by=By.XPATH,
                                                         value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").get_attribute(
            "textContent")
        assert emergency_contactrelation == "Brother"
        emergency_contactnumber = self.driver.find_element(by=By.XPATH,
                                                             value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div").get_attribute(
            "textContent")
        assert emergency_contactnumber == "9856932145"


    def test_employee_dependencies(self, booting_function):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
            "Admin")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
            "admin123")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(
            "233")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys(
            "Megha")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div/input").send_keys(
            "2000-06-06")
        time.sleep(15)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]").click()
        time.sleep(15)
        Dependencies_name = self.driver.find_element(by=By.XPATH,
                                                     value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div").get_attribute(
            "textContent")
        assert Dependencies_name == "Megha"
        time.sleep(3)
        Dependencies_relation = self.driver.find_element(by=By.XPATH,
                                                         value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").get_attribute(
            "textContent")
        assert Dependencies_relation == "Child"

        time.sleep(3)
        emergency_number = self.driver.find_element(by=By.XPATH,
                                                    value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div").get_attribute(
            "textContent")
        assert emergency_number == "2000-06-06"

    def test_employee_jobdetails(self, booting_function):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
            "Admin")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
            "admin123")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(
            "233")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys(
            "2022-12-31")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[18]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[7]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(15)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div[2]/div[3]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]/i").click()

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[3]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div[2]/div[4]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/label/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input").send_keys(
            "2022-12-31")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input").send_keys(
            "2025-12-31")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click()
        time.sleep(15)

        jobdetails_joindate = self.driver.find_element(by=By.XPATH,
                                                       value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input").get_attribute(
            "value")
        assert jobdetails_joindate == "2022-12-31"
        jobdetails_jobtitle = self.driver.find_element(by=By.XPATH,
                                                       value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]").get_attribute(
            "textContent")
        assert jobdetails_jobtitle == "QA Engineer"
        jobdetails_jobcategory = self.driver.find_element(by=By.XPATH,
                                                          value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]").get_attribute(
            "textContent")
        assert jobdetails_jobcategory == "Professionals"
        jobdetails_subunit = self.driver.find_element(by=By.XPATH,
                                                      value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[1]").get_attribute(
            "textContent")
        assert jobdetails_subunit == "Engineering"
        jobdetails_location = self.driver.find_element(by=By.XPATH,
                                                       value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]").get_attribute(
            "textContent")
        assert jobdetails_location == "HQ - CA, USA"
        jobdetails_employmentstatus = self.driver.find_element(by=By.XPATH,
                                                               value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[1]").get_attribute(
            "textContent")
        assert jobdetails_employmentstatus == "Full-Time Permanent"
        jobdetails_contractstart = self.driver.find_element(by=By.XPATH,
                                                            value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input").get_attribute(
            "value")
        assert jobdetails_contractstart == "2022-12-31"
        jobdetails_contractend = self.driver.find_element(by=By.XPATH,
                                                          value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input").get_attribute(
            "value")
        assert jobdetails_contractend == "2025-12-31"


    def test_validation_termination_activation(self, booting_function):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
            "Admin")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
            "admin123")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(
            "233")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input").send_keys(
            "2023-01-01")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[3]/div/div[2]/textarea").send_keys(
            "Terminated")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[4]/button[2]").click()
        time.sleep(15)
        Validate_termination = self.driver.find_element(by=By.XPATH,
                                                        value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/p").get_attribute(
            "textContent")
        assert Validate_termination == "Terminated on: 2023-01-01"
        time.sleep(3)
        activate_option = self.driver.find_element(by=By.XPATH,
                                                   value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button").is_displayed()
        assert activate_option == True
        time.sleep(3)

        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button").click()
        time.sleep(3)
        validat_activation=self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button").is_displayed()
        assert validat_activation == True
        time.sleep(3)

    def test_validation_salary(self, booting_function):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
            "Admin")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
            "admin123")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(
            "233")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys(
            "CTC")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[4]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i").click()

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]").click()

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input").send_keys(("50000"))

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/textarea").send_keys(
            ("Nil"))

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/label/span").click()

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input").send_keys("0915256665856696")

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div/div[2]/i").click()

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]").click()

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input").send_keys("120235696")

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input").send_keys(
            "50000")

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button[2]").click()

        time.sleep(15)

        salary_components = self.driver.find_element(by=By.XPATH,
                                                   value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div").get_attribute("textContent")
        assert salary_components == "CTC"
        time.sleep(3)
        salary_amount =self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").get_attribute("textContent")
        assert salary_amount == "50000"
        time.sleep(3)
        salary_currency = self.driver.find_element(by=By.XPATH,
                                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div").get_attribute(
            "textContent")
        assert salary_currency == "United States Dollar"
        time.sleep(3)
        pay_frequency = self.driver.find_element(by=By.XPATH,
                                                   value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div").get_attribute(
            "textContent")
        assert pay_frequency == "Monthly"
        time.sleep(3)
        direct_deposites = self.driver.find_element(by=By.XPATH,
                                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[6]/div").get_attribute(
            "textContent")
        assert direct_deposites == "50000.00"
        time.sleep(3)

    def test_validation_taxexemption(self, booting_function):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
            "Admin")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
            "admin123")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(
            "233")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(
            "12")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div[25]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input").send_keys(
            "24")

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/i").click()

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div[2]/div[24]").click()

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[2]/i").click()

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div[2]/div[13]").click()

        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button").click()

        time.sleep(15)



        federalIT_status = self.driver.find_element(by=By.XPATH,
                                                   value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]").get_attribute("textContent")
        assert federalIT_status == "Single"
        time.sleep(3)
        federal_exemption =self.driver.find_element(by=By.XPATH,
                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").get_attribute("value")
        assert federal_exemption == "12"
        time.sleep(3)
        stateIT_state = self.driver.find_element(by=By.XPATH,
                                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/div[1]").get_attribute(
            "textContent")
        assert stateIT_state == "Indiana"
        time.sleep(3)
        stateIT_status = self.driver.find_element(by=By.XPATH,
                                                   value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/div[1]").get_attribute(
            "textContent")
        assert stateIT_status == "Single"
        time.sleep(3)
        state_exemption = self.driver.find_element(by=By.XPATH,
                                                 value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input").get_attribute(
            "value")
        assert state_exemption == "24"
        time.sleep(3)
        unemployment_state = self.driver.find_element(by=By.XPATH,
                                                   value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]").get_attribute(
            "textContent")
        assert unemployment_state == "Illinois"
        time.sleep(3)
        work_state = self.driver.find_element(by=By.XPATH,
                                                     value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[1]").get_attribute(
            "textContent")
        assert work_state == "California"
        time.sleep(3)



s = Test_orangeHRmpage_testing()

