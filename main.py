#!/usr/bin/env python
# encoding: utf-8

import os


from flask import Flask
from flask import render_template
from config import config


def create_app(config_name):
    app = Flask(config_name)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    _dir = os.path.dirname(os.path.abspath(__file__))
    app.template_folder = os.path.join(_dir, 'templates')
    app.static_folder = os.path.join(_dir, 'static')

    return app


app = create_app('default')


@app.route("/")
def resume():
    return render_template('index.html')


@app.route("/admin")
def admin():
    return render_template('admin.html')


if __name__ == "__main__":
    app.run()
