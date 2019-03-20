"""
Created by Alex
"""
from threading import Thread

from flask import current_app, render_template

from app import mail
from flask_mail import Message


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_email(to, subject, template, **kwargs):
    """
    Python有标准库提供的email接口，参数过多，使用不方便
    :param to:
    :param subject:
    :param template:
    :param kwargs:
    :return:
    """
    # 测试邮箱
    # msg = Message('测试邮件', sender='feng934879001@163.com', body='Test', recipients=['934879001@qq.com'])
    # mail.send(msg)

    msg = Message('[鱼书]' + ' ' + subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to])
    msg.html = render_template(template, **kwargs)

    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()







