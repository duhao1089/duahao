from selenium.webdriver.common.by import By
from BasePage import *

class LoginPage(Page):
    url=''
    renwu_id=(By.NAME,'taskId')   #定位任务id输入框
    username_loc=(By.NAME,'loginName')   #定位用户名输入框
    password_loc=(By.NAME,'password')   #定位用户名输入框
    submit_loc=(By.TAG_NAME,'button')   #定位登录按钮

    def type_id(self,rid):
        self.find_element(*self.renwu_id).clear()
        self.find_element(*self.renwu_id).send_keys(rid)
    #输入任务id

    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)
    #输入用户名
    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)
    # 输入密码
    def type_submit(self):
        self.find_element(*self.submit_loc).click()
    #点击登录按钮

def test_user_login(driver,rid,username,password):
    login_page=LoginPage(driver)
    login_page.open()
    login_page.type_id(rid)
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_submit()
# 登录功能模块封装