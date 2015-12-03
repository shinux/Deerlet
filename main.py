#!/usr/bin/env python
# encoding: utf-8

import os

from flask import Flask
from flask import render_template
from flask import current_app
from flask import session
from flask import request
from flask import jsonify
from flask import send_from_directory
from flaskext.markdown import Markdown
from markdown import markdown
import pdfkit

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
    title = current_app.config.get('TITLE')
    sub_title = current_app.config.get('SUB_TITLE')
    return render_template('index.html', resume=current_resume, validated=validated, title=title, sub_title=sub_title)


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
        resume = request.json
        if resume:
            with open('resume.md', 'w') as stream:
                stream.write(resume)
            return jsonify(code=1, success=True)
    return jsonify(code=0, success=False)


@app.route("/download", methods=['GET'])
def download():
    input_filename = 'resume.md'
    output_filename = 'resume.pdf'

    output = """<!DOCTYPE html>
    <html lang="zh-cmn-Hans">

    <head>
        <meta charset="UTF-8">
        <style type="text/css">
    """
    with open(current_app.static_folder + '/yue/yue.css', 'r') as yue:
        output += yue.read()
    output += """
        body {
        height: 100%;
        max-height: 100%;
        font-family: "Hiragino Sans GB","Microsoft YaHei","微软雅黑",Georgia,tahoma,arial,simsun,"宋体";
        color: #3A4145;
    }
        .site-head {
        position: relative;
        display: table;
        width: 100%;
        height: 300px;
        margin-bottom: 5rem;
        text-align: center;
        color: #fff;
        background: #303538 no-repeat center center;
        background-size: cover;
    }

    .site-head h1 {
        font-size: 36px;
        line-height: 40px;
    }

    .site-head .subtitle {
        font-size: 24px;
    }

    .vertical {
        display: table-cell;
        vertical-align: middle;
    }
        </style>
    </head>

    <body>
        <header class="site-head">
            <div class="vertical">
                <h1 id="drtitle">"""
    output += current_app.config.get('TITLE')

    output += """</h1>
                <p class="subtitle" id="drsubtitle">"""
    output += current_app.config.get('SUB_TITLE')
    output += """</p>
            </div>
        </header>
    <div class="content yue">
    """

    with open(input_filename, 'r') as stream:
        html_text = markdown(stream.read(), output_format='html4')
    output += html_text
    output += """</div></body>

    </html>
    """
    pdfkit.from_string(output, output_filename, options=current_app.config.get('PDF_OPTIONS'),)

    return send_from_directory(current_app.config.get('UPLOAD_FOLDER'),
                               'resume.pdf', as_attachment=True)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
