#!/usr/bin/env python
# encoding: utf-8

import os

from flask import Flask
from flask import render_template
from flaskext.markdown import Markdown

from config import config


def create_app(config_name):
    app = Flask(config_name)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    Markdown(app)

    _dir = os.path.dirname(os.path.abspath(__file__))
    app.template_folder = os.path.join(_dir, 'templates')
    app.static_folder = os.path.join(_dir, 'static')

    return app


app = create_app('default')


@app.route("/")
def resume():
    with open('resume.md', 'r') as stream:
        resume = stream.read()
    read_password = ''
    return render_template('index.html', resume=resume, password=read_password)


@app.route("/admin")
def admin():
    with open('resume.md', 'r') as stream:
        resume = stream.read()
    return render_template('admin.html', resume=resume)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
