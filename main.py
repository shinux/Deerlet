#!/usr/bin/env python
# encoding: utf-8

import os

from flask import Flask
from flask import render_template
from flask import current_app
from flask import session
from flask import request
from flask import jsonify
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
    if session.get('read_password') == current_app.config.get('READ_PASSWORD'):
        validated = True
        with open('resume.md', 'r') as stream:
            current_resume = stream.read()
    else:
        validated = False
        current_resume = ''
    return render_template('index.html', resume=current_resume, validated=validated)


@app.route("/admin")
def admin():
    if session.get('admin_password') == current_app.config.get('ADMIN_PASSWORD'):
        admin_validated = True
        with open('resume.md', 'r') as stream:
            current_resume = stream.read()
    else:
        admin_validated = False
        current_resume = ''
    return render_template('admin.html', resume=current_resume, admin_validated=admin_validated)


@app.route("/validate", methods=['POST'])
def validate():
    """
    validate read password if True save it into the session
    :return: True：{'success': True, 'code': 1}
             False: {'success': False, 'code': 0}
    """
    read_password = request.json
    true_password = current_app.config.get('READ_PASSWORD')
    if read_password != true_password:
        return jsonify(code=0, success=False)
    else:
        session['read_password'] = read_password
        return jsonify(code=1, success=True)


@app.route("/validate_admin", methods=['POST'])
def validate_admin():
    """
    validate admin password if True save it into the session
    :return: True：{'success': True, 'code': 1}
             False: {'success': False, 'code': 0}
    """
    admin_password = request.json
    true_password = current_app.config.get('ADMIN_PASSWORD')
    if admin_password != true_password:
        return jsonify(code=0, success=False)
    else:
        session['admin_password'] = admin_password
        return jsonify(code=1, success=True)


@app.route("/save", methods=['PUT'])
def save():
    """
    auto save resume into resume.md
    :return: restful suppose we return full content, but i don't want to do this
             True：{'success': True, 'code': 1}
             False: {'success': False, 'code': 0}
    """
    if session.get('admin_password') == current_app.config.get('ADMIN_PASSWORD'):
        print(request.json)
        return jsonify(code=1, success=True)
    else:
        return jsonify(code=0, success=False)


@app.route("/download", methods=['GET'])
def download():
    pass


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
