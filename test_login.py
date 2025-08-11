from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://10.1.2.14:8080/#/login')
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    def test_login(self):
        username=self.driver.find_element(By.ID,'username')
        username.clear()
        username.send_keys('admin')
        password=self.driver.find_element(By.ID,'password')
        password.clear()
        password.send_keys('123456')
        self.driver.find_element(By.XPATH,'//*[@id="loginbutton"]').click()
        DY=self.driver.find_element(By.XPATH,'//*[@id="breadcrumb-container"]/span/span/span[1]/span')
        assert "首页"==DY.text