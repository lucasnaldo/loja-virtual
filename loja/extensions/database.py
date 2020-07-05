# -*- coding: utf-8 -*-
import os

from pathlib import Path

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app, criar_tabelas=False):
    basedir = Path(__file__).parent.parent.parent
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'brprev.db')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    if criar_tabelas:
        with app.app_context():
            db.create_all()

    return app
