# @Time:2021/3/23 9:59 上午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import requests
import pytest
import allure
from common.requests_handler import RequestsHandler


@allure.feature("登录接口校验")
class Test_Login():
    @allure.story("密码错误情况校验")
    @pytest.mark.run(order=3)
    @pytest.mark.login
    # @pytest.mark.login()
    def test_loginInterface_fail(self):
        # 请求类实体化
        self.req = RequestsHandler()
        # 关闭session
        self.req.close_session()
        login_url = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login&t=0.6533599798088903"
        payload = {
            "username": "13800138006",
            "password": "12345",
            "verify_code": "1111"
        }

        res = self.req.visit('post', login_url, json=payload)
        assert "登陆成功" in res['msg']

    @allure.story("密码正确情况校验")
    @pytest.mark.run(order=4)
    @pytest.mark.login
    def test_loginInterface_success(self):
        self.req = RequestsHandler()
        self.req.close_session()
        login_url = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login&t=0.6533599798088903"
        payload = {
            "username": "13800138006",
            "password": "123456",
            "verify_code": "1111"
        }

        res = self.req.visit('post', login_url, json=payload)
        assert "登陆成功" in res['msg']

        


if __name__ == '__main__':
    pytest.main(['-vs', 'test_loginfail.py'])
