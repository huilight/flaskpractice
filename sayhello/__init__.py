from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

app = Flask('sayhello')
app.config.from_pyfile('settings.py')

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)

# 这些模块需要从构造文件中导入程序实例
# 为避免循环依赖，将这些导入语句放在文件的末尾定义
from sayhello import views, errors, commands