# @Time:2021/2/4 10:43
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import yaml
import os
datas = None
# 读取数据驱动的数据
filename = os.path.split(os.path.dirname(__file__))[0] + '/data/UI/login.yaml'


with open(filename, encoding='utf8') as f:
    datas = yaml.safe_load(f)
print(datas)


#测试用
# datas = datas['loginPage'][0]
# testcases = datas['cases']
# for cases in testcases:
#     listcase = list(cases.values())
#     print(listcase)
