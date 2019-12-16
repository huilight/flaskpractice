import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL',
        'sqlite:///'+os.path.join(app.root_path, 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)


>>> from sqlalchemy.schema import CreateTable
>>> print(CreateTable(Note.__table__))
CREATE TABLE note (
    id INTEGER NOT NULL,
    body TEXT,
    PRIMARY KEY (id)
)

import click
...
@app.cli.command()
def initdb():
    db.create_all()
    click.echo('Initialized database.')

from app import db, Note

notel = Note(body='remember Sammy Jankis')
note2 = Note(body='SHAVE')
note3 = Note(body="DON'T BELIEVE HIS LIES.")

db.session.add(notel)
db.session.add(note2)
db.session.add(note3)
# db.session.add_all([notel, note2, note3])
db.session.commit()



filter()
    使用指定的规则过滤记录，返回新产生的查询对象
        Note.query.filter(body=='SHAVE').first()
filter_by()
    使用指定规则过滤记录(以关键字表达式的形式)，返回新产生的查询对象
order_by()
    根据指定条件对记录进行排序，返回新产生的查询对象
limit(limit)
    使用指定的值限制原查询返回的记录数量，返回新产生的查询对象
group_by()
    根据指定条件对记录进行分组，返回新产生的查询对象
offset( offset)
    使用指定的值偏移原查询的结果，返回新产生的查询对象


LIKE:
    filter(Note.body.like('%foo%'))
IN:
    filter(Note.body.in(['foo', 'bar', 'baz']))
NOT IN:
    filter (~Note.body.in(['foo', 'bar', 'baz']))
AND:
# 使用 and()
from sqlalchemy import and_
filter(and_(Note.body == 'foo', Note.title == 'FooBar'))
# 或在filter()中加入多个表达式，使用逗号分隔
filter(Note.body == 'foo', Note.title == 'FooBar')
# 或叠加调用多个filter() / filter_by ()方法
filter(Note.body == 'foo').filter(Note.title == 'FooBar')
OR:
from sqlalchemy import or_
filter(or_(Note.body == 'foo', Note.body == 'bar'))


>> note = Note.query.get(2)
>> note.body
u'SHAVE'
>> note.body = 'SHAVE LEFT THIGH'
>> db.session.commit()

note = Note.query.get(2)
db.session.delete(note)
db.session.commit()