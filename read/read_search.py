# @Time:2021/2/4 15:02
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import yaml
import os
datas1 = None
# 读取数据驱动的数据
filename = os.path.split(os.path.dirname(__file__))[0] + '/data/UI/search.yaml'

with open(filename, encoding='utf8') as e:
    datas = yaml.safe_load(e)
print(datas)

# 测试用
# datas = datas['searchaPage'][0]
# testcases = datas['cases']
# for cases in testcases:
#     listcase = list(cases.values())
#     print(listcase)