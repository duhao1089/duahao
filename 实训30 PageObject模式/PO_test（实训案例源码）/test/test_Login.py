from time import sleep
from selenium import webdriver
from Page2.LoginPage import *


driver=webdriver.Chrome()

test_user_login(driver,'admin','admin')
#输入用户名和密码
sleep(3)

driver.quit()