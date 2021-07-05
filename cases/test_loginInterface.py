# @Time:2021/3/23 9:59 上午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8
import json

import requests
import pytest
import allure
from common.requests_handler import RequestsHandler
from read import read_userInterface


@allure.feature("登录接口校验")
class Test_Login():
    @pytest.mark.parametrize('data', read_userInterface.load('./data/Interface/user.yaml'))
    @pytest.mark.run(order=3)
    @pytest.mark.login
    def test_loginInterface(self, data):
        # 请求类实体化
        self.req = RequestsHandler()
        # 关闭session
        self.req.close_session()
        login_url = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login&t=0.6533599798088903"

        res = self.req.visit('post', login_url, json=data['user'])
        msg = res['msg']
        # 断言失败抛出异常，输出"断言失败"
        # try:
        #     assert data["msg"] == msg
        # except:
        #     print("断言失败")
        # print(res)
        assert data['msg'] == msg
        print(res)


if __name__ == '__main__':
    pytest.main(['test_loginInterface.py'])
