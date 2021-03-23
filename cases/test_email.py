# @Time:2021/2/13 14:58
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import pytest
import allure
import smtplib  # 发送邮箱库
from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header  # 定义邮件标题


class Test_Email():
    @allure.story("发送邮件")
    @pytest.mark.login
    @pytest.mark.run(order=9)
    def test_email(self):
        # 发送邮箱服务器
        smtpserver = 'smtp.qq.com'

        # 发送邮箱用户/密码(登录邮箱操作)
        user = "2734259470@qq.com"
        password = "xnhphqoxeyuddegf"  # 这里是授权码，不是密码

        # 发送邮箱
        sender = "2734259470@qq.com"

        # 接收邮箱
        receiver = "2734259470@qq.com"

        # 发送主题
        subject = '测试完成'

        # 编写HTML类型的邮件正文（把HTML代码写进入）
        msg = MIMEText('<html><body><a href="">测试已经完成，请到Jenkins服务器查看allure报告</a></p></body></html>', 'html', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')

        # 连接发送邮件（smtplib模块基本使用格式）
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()


if __name__ == '__main__':
    pytest.main(['test_email.py'])
