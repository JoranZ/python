
import time

import pytest
import xlrd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

class WX():

    def get_cokkies(self):
        option=Options()
        option.debugger_address='localhost:9222'
        driver=webdriver.Chrome(options=option)
        cookies=str(driver.get_cookies())
        with open('./cookies.py','w') as f:
            f.writelines(cookies)



    def import_contact(self):
        driver = webdriver.Chrome()
        url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
        driver.get(url)

        with open('./cookies.py') as f:
            cookies = eval(f.readline())
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get(url)
        while True:
            try:
                WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("party_name"))
                driver.find_element('xpath',"//*[@id='party_name']").text=='IT测试公司'
                break
            except:
                driver.refresh()
                WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("party_name"))
                driver.find_element('xpath', "//*[@id='party_name']").text == 'IT测试公司'
                break




        driver.find_elements('xpath',"//*[@class='ww_btn_PartDropdown_left']")[1].click()
        driver.find_element('link text','文件导入').click()
        driver.find_element('xpath',"//*[@type='file']").send_keys(r'D:\通讯录.xlsx')
        driver.find_element('link text','导入').click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_link_text("完成")).click()
        time.sleep(2)

        names = driver.find_elements('xpath', "//*[@class='js_unsortable js_list']/tr/td[2]")
        peoples=[]
        for name in names:
            i = name.get_attribute('title')
            peoples.append(i)
        return peoples

    def read_telphone_xls(self):
        book=xlrd.open_workbook(r'D:\通讯录.xlsx')
        sheet=book.sheet_by_name('成员列表')
        rows=sheet.nrows
        name=[]
        for row in range(1,rows):
            i=sheet.row_values(row)
            name.append(i[0])
        return name

class Test_WX():
    names=WX().import_contact()
    xls=WX().read_telphone_xls()
    @pytest.mark.parametrize('name',names)
    def test_01(self,name):
        assert name in self.xls


















