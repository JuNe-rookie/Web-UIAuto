# @Time:2021/3/24 10:19 上午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import yaml


# 公共读取yaml文件
def load(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data
