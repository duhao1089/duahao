from time import sleep

class Page():
    """基础类，用于所以页面对象类继承"""
    def __init__(self,driver):
        self.driver=driver
        self.base_url='http://192.168.5.10/ams/front/login.do'
        self.timeout=10

    def _open(self,url):
        url_=self.base_url+url
        print("Test page is %s" %url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url==url_ ,'Did not land on %s' %url_

    def open(self):
        self._open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    