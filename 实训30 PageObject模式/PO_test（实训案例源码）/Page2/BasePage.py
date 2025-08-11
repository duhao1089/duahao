from time import sleep


class Page():
    """基础类，用于所以页面对象类继承"""
    def __init__(self,driver):
        self.driver=driver
        self.base_url='https://lite.yfhl.net/'



    def _open(self,url):
        url_=self.base_url+url

        self.driver.get(url_)
        sleep(2)


    def open(self):
        self._open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    