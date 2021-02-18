# @Time:2021/2/4 14:19
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import allure
from common.initialization import Comm
import pytest
from read.read_userinfo import datas


@allure.feature("用户信息")
class Test_Userinfo():  # 这是查看个人信息的类

    @allure.story("打开浏览器")
    def setup_class(self):
        self.web = Comm()
        self.web.openbrowser()

        pass

    @pytest.mark.parametrize('listcases', datas['userinfoPage'])
    @allure.story("我的")
    @pytest.mark.login
    @pytest.mark.run(order=3)
    def test_userinfo(self, listcases):
        allure.dynamic.title(listcases['title'])  # 获取yaml中的title
        testcase = listcases['cases']
        for cases in testcase:
            listcases = list(cases.values())  # 获取字典列表值
            with allure.step(listcases[0]):
                func = getattr(self.web, listcases[1])
                values = listcases[2:]
                print("values = ", values)
                func(*values)
            self.web.sleep(2)  # 强制等待4s，防止因为网络原因加载失败
        # self.web.quit()


if __name__ == '__main__':
    pytest.main(['test_userinfo.py'])
