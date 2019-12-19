import os
from flask import Flask, redirect, render_template, url_for  # noqa
from flask_sqlalchemy import SQLAlchemy  # noqa
from forms import NewNoteForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 'sqlite:///' +
        os.path.join(app.root_path, 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dsf2o3o9KJFO#0f02f'
db = SQLAlchemy(app)


@app.route('/new', methods=['GET', 'POST'])
def new_note():
    form = NewNoteForm()
    if form.validate_on_submit():
        body = form.body.data
        note = Note(body=body)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_note.html', form=form)


@app.route('/')
def index():
    # form = DeleteForm()
    notes = Note.query.all()
    return render_template('index.html', notes=notes)
