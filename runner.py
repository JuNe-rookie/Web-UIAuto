# @Time:2021/2/2 17:29
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import pytest
import os
import shutil
import allure
# from read.read_login import datas

# print(datas)


if __name__ == '__main__':
    print("===============================    开始执行测试    ===============================")
    pytest.main(['-s', '-q', '-m login', '--alluredir', './temp'])

    print("===============================    执行测试结束    ===============================")

    print("==============================    正在生成测试报告    =============================")
    shutil.copy('/Users/liuyue/Desktop/刘岳/pythonProjectSEle/environment.properties',
                r'/Users/liuyue/Desktop/刘岳/pythonProjectSEle/temp')
    os.system('allure generate ./temp -o ./report --clean')

    # shutil.copy('/Users/liuyue/Desktop/刘岳/pythonProjectSEle/environment.properties',
    #             r'/Users/liuyue/Desktop/刘岳/pythonProjectSEle/report')

    print("=====================    测试报告生成功，请在report中查看    ========================")
