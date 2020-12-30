from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver=None):
        option=Options()
        option.debugger_address='localhost:9222'
        self.driver=webdriver.Chrome(options=option)

    def find_element(self,loctor):
        num=1
        while True:
            if num<=5:
                try:
                    elment=WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loctor))
                    return elment
                    break
                except:
                    self.driver.refresh()
                    elment = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loctor))
                    return elment
                    break
            else:
                print(f'未定位到元素:{loctor}')
                break


    def find_elements(self,loctor):
        num = 1
        while True:
            if num <= 5:
                try:
                    elments = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*loctor))
                    return elments
                    break
                except:
                    self.driver.refresh()
                    elments = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*loctor))
                    return elments
                    break
            else:
                print(f'未定位到元素:{loctor}')
                break
    def send(self,loctor,value):
        element=self.find_element(loctor).send_keys(value)
        return element
    def click(self,loctor):
        element=self.find_element(loctor).click()
        return element
    def clicks(self,loctor):
        elements = self.find_elements(loctor).click()
        return elements