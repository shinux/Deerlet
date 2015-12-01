#!/usr/bin/env python
# encoding: utf-8

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base Configuration"""

    TITLE = '我是 title'
    SUB_TITLE = '我是 subtitle'
    MAX_LENGTH = '10000'

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
