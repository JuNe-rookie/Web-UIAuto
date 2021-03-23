# @Time:2021/3/23 10:00 上午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import requests


# 存放session
class RequestsHandler:
    def __init__(self):
        """session管理器"""
        self.session = requests.session()

    def visit(self, method, url, params=None, data=None, json=None, headers=None):
        result = self.session.request(method, url, params=params, data=data, json=json, headers=headers)
        try:
            # 返回json结果
            return result.json()
        except Exception:
            return 'not json'

    def close_session(self):
        self.session.close()