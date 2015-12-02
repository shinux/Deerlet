#!/usr/bin/env python
# encoding: utf-8

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base Configuration"""

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'deerletisawesome'  # Modify your SECRET KEY 建议足够复杂

    TITLE = '我是 title'  # 简历标题
    SUB_TITLE = '我是 subtitle'  # 简历子标题
    MAX_LENGTH = '10000'  # 简历字数限制
    READ_PASSWORD = '12345'  # 简历浏览密码
    ADMIN_PASSWORD = 'abcd'  # 简历管理密码

    @classmethod
    def init_app(cls, app):
        pass


class ModifiedConfig(Config):
    """Modified Your Configuration"""

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        import logging
        from logging import FileHandler

        syslog_handler = FileHandler(os.path.join(basedir, 'logs/deerlet.log'))
        syslog_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(syslog_handler)


config = {
    'modified': ModifiedConfig,
    'default': ModifiedConfig,
}
