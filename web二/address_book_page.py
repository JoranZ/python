
from python.web二.base import Base

class Address_Book(Base):
    def add_option(self,name):
        _add = ('css selector', ".member_colLeft_top_addBtn")  # 添加按钮
        _add_dep = ('link text', '添加部门')  # 添加部门
        _name = ('xpath', "//*[@name='name']")  # 输入部门名字
        _select_dep = ('xpath', "//*[text()='选择所属部门']")  # 选择所属部门下拉框
        # _department=(('xpath',"//*[@class='jstree-anchor']")[1])
        _department = ('xpath', "//*[@class='jstree-anchor' and @id='1688850241689713_anchor']")  # 选择部门

        # self.click(_add)
        # self.click(_add_dep)
        # self.send(_name, name)
        # self.click(_select_dep)
        # self.click(_department)

    def add_affirm (self,name):
        _affirm = ('link text', '确定')  # 确定按钮
        _all_name=('xpath',"//ul[@class='jstree-children']//li") #一级部门列表
        self.add_affirm(name)
        self.click(_affirm)
        all=self.find_elements(_all_name)
        return [i.text for i in all]
    def add_cancel(self,name):
        _cancel=('link text', '取消')
        _all_name = ('xpath', "//ul[@class='jstree-children']//li")  # 一级部门列表
        self.add_affirm(name)
        self.click(_cancel)
        all = self.find_elements(_all_name)
        return [i.text for i in all]




if __name__ == '__main__':
    a=Address_Book()
    a.add_option('test')