### 为什么不用 DeerResume

[DeerResume](https://github.com/geekcompany/DeerResume) 是国内很火的一个“开源”简历模板。

DeerResume 的一切数据都保存在 http://cvbox.sinaapp.com/ 这个 sae 的云端，是的，并且在 `app.js` 中：

```js
var baseurl = 'http://cvbox.sinaapp.com/'; // 使用SAE托管简历数据
// var baseurl = 'data.php'; // 使用本地文件托管简历数据，本地模式下，不支持在线编辑
```

我们不去猜测这么多保存在云端的简历会被拿去做什么，但是这个本地的 data.php 基本上没什么用处，在离线的情况下（本地调试)，我甚至不能编辑，修改和查看我自己的简历, 因为它根本就不存在。

而打印服务，也是放在远端，依赖一个 http://pdf.ftqq.com/ 的 pdf.js 展示，并提供下载服务，是的。

如果你用这个服务下载了 pdf ，那么这个文件的底端还有水印。

这些理由已经足够让我不去使用它了，更不要说阅读密码和管理密码的传输方式，参见 [issue](https://github.com/geekcompany/DeerResume/issues/12)

### Deerlet

Deerlet 是一个在线简历模板，提供在线展示，编辑，打印 pdf 服务（无水印：），密码写死在后台配置文件并在 session 中保存和验证，不需要任何数据库。

[DEMO | 在线预览](http://sinux.cc) (阅读密码： 1234, 管理密码: abcd）

- 后端基于：[Flask](https://github.com/mitsuhiko/flask),   [Flask-Markdown](https://github.com/dcolish/flask-markdown)
- 前端基于：[yue.css](https://github.com/lepture/yue.css),   [editor.md](https://github.com/pandao/editor.md)
- pdf打印服务基于：[pdfkit](https://github.com/JazzCore/python-pdfkit),   [wkhtmltopd](fhttp://wkhtmltopdf.org/)

(resume.md 的基本模板仅作为参考)

### 下载及部署

(由于淘汰 Python2 人人有责，所以 Deerlet 只支持 Python3 )

依赖 Python3 环境。

克隆 Deerlet:

    git clone git@github.com:shnode/Deerlet.git && cd Deerlet

安装第三方包（最好在virtualenv中）：

    pip install -r requirements.txt

安装 pdf 打印服务的依赖 `wkhtmltopdf`:

    osx/windows : 在 [http://wkhtmltopdf.org/downloads.html](http://wkhtmltopdf.org/downloads.html) 下载的对应版本并安装。

    DEB 系 linux: sudo apt-get install wkhtmltopdf

    其余 linux 查询相关包管理或去 [http://wkhtmltopdf.org/downloads.html](http://wkhtmltopdf.org/downloads.html) 下载.

运行：

    Python3 main.py

    open "http://127.0.0.1:5000" # 访问 http://127.0.0.1:5000

### 配置

建议在使用之前，进行配置。配置集中在 Deerlet 的项目根目录下的 config.py 中：


    SECRET_KEY = os.environ.get('SECRET_KEY') or 'deerletisawesome'  # Modify your SECRET KEY 建议足够复杂

    TITLE = 'Deerlet'  # 简历标题，例：马云的简历
    SUB_TITLE = '基于 Python 的开源简历模板'  # 简历子标题，一句话介绍自己，例：好的东西往往都是很难描述的。
    READ_PASSWORD = '12345'  # 简历浏览密码
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
    }  # PDF 设置

在线编辑模式下，每 6 秒自动保存一次当前的文本（全文保存），如果你想修改这个数值，在 `admin.html` 的第 35 行进行修改：

    setInterval("saveToFile()", 6000);  // 修改自动保存的时间

一切简历数据（除了标题）保存在 `resume.md` 中，如果喜欢，你也可以离线编辑，并且 copy 到任何地方。

### License

**GPLv2**
