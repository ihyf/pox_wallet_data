# coding:utf-8
from sqlalchemy import Column
from sqlalchemy import Integer, String, Text, JSON, DATETIME, ForeignKey, PickleType, DateTime, text
from util.dbmanager import db_manager
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    address = Column(String(80), unique=True)

    def __repr__(self):
        return '<Account %r>' % self.address


class RecodeLogs(Base):
    __tablename__ = "recode_logs"
    rl_id = Column(Integer, autoincrement=True, primary_key=True)
    create_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    level_name = Column(String(10))
    message = Column(String(255))
    func_name = Column(String(255))
    stack_info = Column(String(255))


# class Apps(Base):
#     __tablename__ = 'apps'
#     id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
#     appid = Column(String(200), primary_key=True, nullable=False, unique=True)
#     parent_appid = Column(String(200), nullable=False, default="unknow")
#     desc = Column(String(200), nullable=False)
#     ip = Column(JSON, nullable=False)
#     ns = Column(JSON, nullable=False)
#     cli_publickey = Column(Text, nullable=False)
#     cli_privatekey = Column(Text, nullable=False)
#     srv_publickey = Column(Text, nullable=False)
#     srv_privatekey = Column(Text, nullable=False)
#     srv = Column(JSON, nullable=False)
#     master_contract_address = Column(JSON, nullable=False, default=[])
#     wallet = Column(String(200), nullable=False, default="no set")
#     callback_url = Column(String(250), nullable=True)
#     status = Column(Integer, nullable=False)

    
def create_tables():
    engine = db_manager.get_engine_master()
    Base.metadata.create_all(engine)


