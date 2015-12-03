#!/usr/bin/env python
# encoding: utf-8

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base Configuration"""

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'deerletisawesome'  # Modify your SECRET KEY 建议足够复杂

    TITLE = 'Deerlet'  # 简历标题，例：马云的简历
    SUB_TITLE = '基于 Python 的开源简历模板'  # 简历子标题，一句话介绍自己，例：好的东西往往都是很难描述的。
    READ_PASSWORD = ''  # 简历浏览密码
    ADMIN_PASSWORD = 'abcd'  # 简历管理密码
    BASE_DIR = basedir
    UPLOAD_FOLDER = basedir

    PDF_OPTIONS = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None
    }

    @classmethod
    def init_app(cls, app):
        pass


class ModifiedConfig(Config):
    """Modified Your Configuration"""

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'modified': ModifiedConfig,
    'default': ModifiedConfig,
}
