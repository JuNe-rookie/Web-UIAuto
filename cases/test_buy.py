# @Time:2021/2/7 15:08
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

from read.read_buy import datas
import allure
from selenium import webdriver

from common.initialization import Comm
import pytest


@allure.feature("购买物品")
class Test_Search():

    @allure.story("打开浏览器")
    def setup_class(self):
        self.web = Comm()
        self.web.openbrowser()

        pass

    @pytest.mark.parametrize('listcases2', datas['buyPage'])
    @allure.story("购买物品")
    @pytest.mark.login
    @pytest.mark.run(order=6)
    def test_search(self, listcases2):
        allure.dynamic.title(listcases2['title'])  # 获取yaml中的title
        testcase = listcases2['cases']
        for cases in testcase:
            listcases2 = list(cases.values())  # 获取字典列表值
            with allure.step(listcases2[0]):
                func = getattr(self.web, listcases2[1])
                values = listcases2[2:]
                func(*values)
            self.web.sleep(4)  # 强制等待4s，防止因为网络原因加载失败


if __name__ == '__main__':
    pytest.main(['test_buy.py'])
