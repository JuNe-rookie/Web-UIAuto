# @Time:2021/2/3 09:40
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Comm:
    def __init__(self):
        self.driver = None  # 初始化浏览器驱动

    def openbrowser(self, br='gc'):  # 打开浏览器
        """
        确认浏览器
        :param br: gc=谷歌浏览器；ff=Firefox浏览器；ie=IE浏览器
        :return:
        """

        # 谷歌复用浏览器，可以在一个页面执行多个case，不用再次打开新窗口导致需要再次登陆
        # 浏览器复用目前只支持谷歌浏览器ß
        if br == 'gc':
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            # self.driver = webdriver.Chrome()
        elif br == 'ff':
            self.driver = webdriver.Firefox()
        elif br == 'ie':
            self.driver = webdriver.Ie()
        else:
            print('浏览器暂不支持')

        self.driver.implicitly_wait(8)  # 隐性等待8s

    def geturl(self, url=None):
        """
        打开网站
        :param url:网站链接
        :return:
        """
        self.driver.get(url)

    def __find_ele(self, locator=''):
        """
        支持八种定位方式
        :param locator:Xpath=//*[@id="username"]
        :return: 返回定位到的元素
        """
        ele = None
        self.ele = None
        if locator.startswith('xpath='):
            ele = self.driver.find_element_by_xpath(locator[locator.find('=') + 1:])
        elif locator.startswith('id='):
            ele = self.driver.find_element_by_id(locator[locator.find('=') + 1:])
        elif locator.startswith('name='):
            ele = self.driver.find_element_by_name(locator[locator.find('=') + 1:])
        elif locator.startswith('tag_name='):
            ele = self.driver.find_element_by_tag_name(locator[locator.find('=') + 1:])
        elif locator.startswith('link_text='):
            ele = self.driver.find_element_by_link_text(locator[locator.find('=') + 1:])
        elif locator.startswith('partial_link_text='):
            ele = self.driver.find_element_by_partial_link_text(locator[locator.find('=') + 1:])
        elif locator.startswith('css_selector='):
            ele = self.driver.find_element_by_css_selector(locator[locator.find('=') + 1:])
        else:
            ele = self.driver.find_element_by_xpath(locator)

        self.ele = ele
        return ele

    def click(self, locator=None):
        """
        找到并点击元素
        :param locator: 定位器，默认Xpath
        :return:
        """
        ele = self.__find_ele(locator)
        ele.click()

    def input(self, locator=None, value=None):
        """
        找到元素，输入
        :param locator: 定位器，默认Xpath
        :param value: 需要输入的字符串
        :return:
        """
        ele = self.__find_ele(locator)
        ele.send_keys(str(value))

    def clear(self, locator=None):
        """
        清除输入框文本
        :param locator:
        :return:
        """
        ele = self.__find_ele(locator)
        ele.clear()

    def intoifarme(self, locator=None):
        """
        进入iframe，作用：切换弹窗
        :param locator: 定位器，默认Xpath
        :return:
        """
        ele = self.__find_ele(locator)
        self.driver.switch_to.frame(ele)

    def quit(self):
        """
        退出浏览器
        :return:
        """
        self.driver.quit()

    def max(self):
        """
        浏览器最大化
        :return:
        """
        self.driver.maximize_window()

    def wait(self, t=8):
        """
        隐性等待（S）
        :return:
        """
        self.driver.implicitly_wait(int(t))

    def sleep(self, t=1):
        """
        固定等待
        :param t: 强制等待（S）
        :return: 
        """
        time.sleep(int(t))

    def title(self):
        """
        获取当前页面title
        :return:title
        """
        return self.driver.title

    def shot(self):
        """
        截图
        :return:
        """
        self.driver.get_screenshot_as_png()

    def currentPageUrl(self):
        """
        获取当前页面url
        :return:currentPageUrl
        """
        return self.driver.current_url

    def pageSource(self):
        """
        获取当前页面源码
        :return:pageSource
        """
        return self.driver.page_source
