# @Time:2021/2/2 16:56
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import allure
from selenium import webdriver

from common.initialization import Comm
import pytest
from read.read_loginfail import datas


@allure.feature("用户登陆失败")
class Test_Loginfail():  # 这是一个登陆模块的类

    @allure.story("打开浏览器")
    def setup_class(self):
        self.web = Comm()
        self.web.openbrowser()
        self.web.max()
        # self.web.title()

    @pytest.mark.parametrize('listcases', datas['loginfailPage'])
    @allure.story("用户登陆")
    @pytest.mark.login
    @pytest.mark.run(order=1)
    def test_loginfail(self, listcases):
        allure.dynamic.title(listcases['title'])  # 获取yaml中的title

        testcase = listcases['cases']
        for cases in testcase:
            listcases = list(cases.values())  # 获取字典列表值
            with allure.step(listcases[0]):
                func = getattr(self.web, listcases[1])
                values = listcases[2:]
                func(*values)
            self.web.sleep(2)

        url = self.web.currentPageUrl()
        print("当前页面的url是：", url)
        assert url == "http://www.testingedu.com.cn:8000/index.php/Home/User/index.html"
        # return url
        # self.web.quit()


if __name__ == '__main__':
    pytest.main(['test_loginfail.py'])
