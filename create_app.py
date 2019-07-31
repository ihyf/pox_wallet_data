# coding:utf-8
from flask import Flask
from flask_cors import CORS
import config
from my_dispatcher import api
from api import *
from werkzeug.contrib.fixers import ProxyFix
from util.db_redis import redis_store
from util.dbmanager import db_manager
from util.mysql_db import create_tables


async_mode = None


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api.as_blueprint(url='/api'))
    # 跨域请求
    CORS(app, supports_credentials=True)
    app.config['DEBUG'] = config.DEBUG
    # app.config['SQLALCHEMY_BINDS'] = config.SQLALCHEMY_BINDS
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SQLALCHEMY_DATABASE_URI_SETTINGS'] = config.SQLALCHEMY_DATABASE_URI_SETTINGS
    app.config['REDIS_URL'] = config.REDIS_URL
    return app


app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)


with app.app_context():
    db_manager.init_app(app)
    redis_store.init_app(app)
    # create_tables()   # 手动创建数据库表
    pass

