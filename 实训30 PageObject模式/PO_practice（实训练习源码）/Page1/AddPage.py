from selenium.webdriver.common.by import By
from BasePage import *
from time import sleep
class AddC(Page):
    url='/'
    Bumen_loc=(By.LINK_TEXT,'部门管理')    #定位部门管理按钮
    Add_loc=(By.XPATH,'//*[@id="content"]/div[2]/div/div[1]/button')      #定位新增按钮
    Name_loc=(By.ID,'title')   #定位部门名称输入框
    Bianma_loc=(By.ID,'code')        #定位部门编码输入框
    Baocun_loc=(By.ID,'submitButton')       #定位保存按钮

    def type_Bumen(self):
        self.find_element(*self.Bumen_loc).click()
    #点击部门管理按钮
    def type_Add(self):
        self.find_element(*self.Add_loc).click()
    #点击新增按钮

    def type_Name(self,Name):
        self.find_element(*self.Name_loc).clear()
        self.find_element(*self.Name_loc).send_keys(Name)
    #输入部门名称
    def type_Bianma(self,Bian):
        self.find_element(*self.Bianma_loc).clear()
        self.find_element(*self.Bianma_loc).send_keys(Bian)
    #输入部门名称
    def type_Baocun(self):
        self.find_element(*self.Baocun_loc).click()
    # 点击保存按钮

def test_user_add(driver,Name,Bian):
    add_page=AddC(driver)
    add_page.type_Bumen()
    add_page.type_Add()
    sleep(1)
    add_page.type_Name(Name)
    add_page.type_Bianma(Bian)
    add_page.type_Baocun()
