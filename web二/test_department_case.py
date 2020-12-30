import allure
import pytest
from python.web二.address_book_page import Address_Book
@allure.feature('添加通讯录')
class Test_AddressBook():
    @allure.story('添加成功')
    def test_add_department01(self):
        result=Address_Book().add_affirm('test')
        assert 'test' in result
    @allure.story("添加重复的部门")
    def test_add_department02(self):
        result = Address_Book().add_affirm('test')
        assert result.count('test')<2
    @allure.story("取消添加")
    def test_add_department03(self):
        result =Address_Book().add_cancel('test01')
        assert 'test01' not in result
