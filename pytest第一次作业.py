'''计算器'''
import os
class Caculator():

    def add (self,a,b):
        if self.is_type(a,b)==1:
            return a+b
        elif self.is_type(a,b)==0:
            return False

    def sub(self,a,b):
        if self.is_type(a, b) == 1:
            return a - b
        elif self.is_type(a, b) == 0:
            return False

    def mul(self,a,b):
        if self.is_type(a, b) == 1:
            return a * b
        elif self.is_type(a, b) == 0:
            return False
    def div(self,a,b):
        if self.is_type(a, b) == 1:
            return a / b
        elif self.is_type(a, b) == 0:
            return False
    def is_type(self,a,b):
        try:
            if type(a) not in [int,float]:
                return 0
            elif type(b) not in [int,float]:
                return 0
            else:
                return 1
        except EOFError as e:
            print(e)

    def read_cvs(self,filename):
        dir=os.path.abspath(r'./data/'+filename)
        num_list=[]
        with open(dir) as f:
            for line in f.readlines():
                num=line.strip().split(',')
                x=num[0]
                y=num[1]
                ex=num[2]
                dic={}
                dic['x']=x
                dic['y']=y
                dic['ex']=ex
                num_list.append(dic)
        return num_list


'''测试用例'''
import pytest
import allure
f=Caculator()
d=Caculator().read_cvs('add.csv')
b=Caculator().read_cvs('mul.csv')
@allure.feature('计算器')
class Test_cacul():
    def setup(self):
        print('***开始计算***')

    def teardown(self):
        print('***计算结束***')
    @allure.story('加法')
    @pytest.mark.parametrize('case',d)
    def test_add(self,case):
        with allure.step('计算结果'):
            result=f.add(eval(case['x']),eval(case['y']))
        with allure.step('期望结果'):
            ex=eval(case['ex'])
        assert result==ex
    @allure.story('乘法')
    @pytest.mark.parametrize('case', b)
    def test_mul(self, case):
        with allure.step("计算结果"):
            result = f.mul(eval(case['x']), eval(case['y']))
        with allure.step("期望结果"):
            ex = eval(case['ex'])
        assert result == ex



'''测试数据add'''
0,0,0
0,9,9
1,9,10
9,9,18
-1,9,8
-1,1,0
-1,-9,-10
1,-9,-8
0,4.5,4.5
0.5,4,4.5
1.3,0.3,1.6
'1',3,False
5,'2',False
1.3,'4',False

'''测试数据mul'''
0,0,0
0,9,0
1,9,9
9,9,81
-1,9,-9
-1,1,-1
-1,-9,9
1,-9,-9
0,4.5,0
0.5,4,2
1.3,0.3,0.39
'1',3,False
5,'2',False
1.3,'4',False






