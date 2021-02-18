# @Time:2021/2/2 16:56
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import allure
from selenium import webdriver

from common.initialization import Comm
import pytest
from read.read_login import datas
import requests


@allure.feature("用户登陆")
class Test_Login():  # 这是一个登陆模块的类

    @allure.story("打开浏览器")
    def setup_class(self):
        self.web = Comm()
        self.web.openbrowser()
        self.web.max()
        # self.web.title()

    @pytest.mark.parametrize('listcases', datas['loginPage'])
    @allure.story("用户登陆")
    @pytest.mark.login
    @pytest.mark.run(order=2)
    def test_login(self, listcases):
        allure.dynamic.title(listcases['title'])  # 获取yaml中的title

        testcase = listcases['cases']
        for cases in testcase:
            listcases = list(cases.values())  # 获取字典列表值
            # allure.attachallure.attach('screenshot',self.web.shot()ß, type='png')

            with allure.step(listcases[0]):
                func = getattr(self.web, listcases[1])
                values = listcases[2:]
                func(*values)
            self.web.sleep(2)

        title = self.web.title()
        print("当前页面的title是：", title)
        assert title == u"我的账户-开源商城 | B2C商城 | B2B2C商城 | 三级分销 | 免费商城 | 多用户商城 | tpshop｜thinkphp shop｜TPshop 免费开源系统 | 微商城"
        # return title

        # self.web.quit()


if __name__ == '__main__':
    pytest.main(['test_login.py'])
