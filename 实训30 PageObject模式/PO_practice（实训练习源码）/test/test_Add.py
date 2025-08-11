from selenium import webdriver
from Page.LoginPage import *
from Page.AddPage import *

driver=webdriver.Chrome()

test_user_login(driver,'1','student','student')
#执行登陆操作
sleep(3)

test_user_add(driver,'测试数据','BM8888')
#执行添加操作

sleep(3)
driver.quit()