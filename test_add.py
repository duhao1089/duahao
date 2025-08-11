from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pytest
from test_login import TestDemo
import allure

class Testadd(TestDemo):
    @pytest.mark.parametrize(
        "main_image_path, carousel_image_path",
        [
            (r"C:\Users\d3484\Desktop\tupian.png", r'C:\Users\d3484\Desktop\tp - 副本.png'),
            (r"C:\Users\d3484\Desktop\tupian.png", r"C:\Users\d3484\Desktop\tp - 副本.png")
        ]
    )
    @allure.story('上传图片模块')
    def test_add(self,main_image_path,carousel_image_path):
        self.test_login()
        self.driver.find_element(By.XPATH ,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span').click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[2]/a/li/span').click()
        self.driver.find_element(By.XPATH ,'//*[@id="pane-first"]/div/div[1]/div[4]/button[1]/span').click()
        self.driver.find_element(By.XPATH ,'//*[@id="app"]/div/div[2]/section/div[1]/div/div/form/div[1]/div[1]/div/div/div[1]/input').send_keys("测试")
        self.driver.find_element(By.XPATH ,'//*[@id="app"]/div/div[2]/section/div[1]/div/div/form/div[1]/div[2]/div/div/div/div/input').click()
        # 直接按文本定位（包含特殊符号也能匹配）
        element = self.driver.find_element(By.XPATH, '//span[text()="|-----|-----健康"]')
        element.click()
        self.driver.find_element(By.XPATH ,'//*[@id="app"]/div/div[2]/section/div[1]/div/div/form/div[1]/div[3]/div/div/div/input').send_keys("123")
        self.driver.find_element(By.XPATH ,'//*[@id="app"]/div/div[2]/section/div[1]/div/div/form/div[1]/div[4]/div/div/div[1]/input').send_keys("教育")
        self.driver.find_element(By.XPATH ,'//*[@id="app"]/div/div[2]/section/div[1]/div/div/form/div[1]/div[5]/div/div/div/textarea').send_keys("123456")
        # 上传图片
        self.driver.find_element(By.XPATH ,'//*[@id="app"]/div/div[2]/section/div[1]/div/div/form/div[1]/div[6]/div/div/div/div[1]').click()
        sleep(2)
        upload_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')
        upload_input.send_keys(main_image_path)
        sleep(1)
        self.driver.find_element(By.XPATH ,'/html/body/div[4]/div/div[2]/section/main/div/div[2]/div/div[1]/div/div[1]/div/div/div[2]/label/span[1]').click()
        self.driver.find_element(By.XPATH ,'/html/body/div[4]/div/div[3]/span/button[2]').click()
        # 上传轮播图
        sleep(2)
        self.driver.find_element(By.XPATH ,'//*[@id="app"]/div/div[2]/section/div[1]/div/div/form/div[1]/div[7]/div/div/div/div[1]').click()
        carousel_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')
        carousel_input.send_keys(carousel_image_path)
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/section/main/div/div[2]/div/div[1]/div/div[1]/div/div/div[2]/label/span[1]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/span/button[2]').click()
        sleep(2)
        self.driver.find_element(By.XPATH ,'//*[@id="app"]/div/div[2]/section/div[1]/div/div/form/div[1]/div[10]/div/div/div/div[3]/table/tbody/tr/td[5]/div/div/input').send_keys('10')
        self.driver.find_element(By.XPATH ,'//*[@id="app"]/div/div[2]/section/div[1]/div/div/form/div[1]/div[10]/div/div/div/div[3]/table/tbody/tr/td[4]/div/div/input').send_keys('2')
        self.driver.find_element(By.XPATH ,'/html/body').send_keys('123')

        self.driver.execute_script('document.evaluate(\'//*[@id="app"]/div/div[2]/section/div[1]/div/div/form/div[4]/div/button/span\', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();')




