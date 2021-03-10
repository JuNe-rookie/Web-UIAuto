# @Time:2021/3/10 10:05
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

from logging import Logger
import allure
from common.initialization import Comm


class NewTestcase():
    # logger = Logger()
    # co = Comm()

    def assertEqual_new(self, first, second, driver, msg=None):
        """
        判断first==second,否则抛错msg
        :param first:
        :param second:
        :param msg:
        :param driver:
        :return:
        """
        self.web = Comm
        try:
            assert first == second, msg
        except Exception as e:
            # self.logger.erro(f"断言失败{str(e)}")
            filename = self.web.save_screen_shot(driver)
            if filename:
                allure.attach.file(filename, '异常截图', allure.attachment_type.PNG)
                raise
