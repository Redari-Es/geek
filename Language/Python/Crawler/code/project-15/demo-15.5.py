from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:1990@127.0.0.1:3306/test?charset=utf8", echo=True)
#创建数据表方法一
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class mytable(Base):
    __tablename__ = 'mytable'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    age = Column(Integer)
    birth = Column(DateTime)
    class_name = Column(String(50))


Base.metadata.create_all(engine)

#方法二
from sqlalchemy import Column, MetaData, ForeignKey, Table
from sqlalchemy.dialects.mysql import (INTEGER, CHAR)

meta = MetaData()
myclass = Table('myclass', meta, Column('id', INTEGER, primary_key=True),
                Column('name', CHAR(50), ForeignKey(mytable.name)),
                Column('class_name', CHAR(50)))

myclass.create(bind=engine)

#删除数据表
#myclass.drop(bind=engine)
#Base.metadata.drop_all(engine)
