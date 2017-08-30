# 导入:
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer(), primary_key=True)
    name = Column(String(20),unique=True)






# 初始化数据库连接:
engine = create_engine('sqlite:///./dict/test.db')
# 创建DBSession类型:
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)

def insert(ob):
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    #new_user = User(name='w4s')
    #添加到session:
    session.merge(ob)
    #session.add(new_user)
    # 提交即保存到数据库:
    try:
        session.commit()
        print('insert success!')
    except:
        print('something error')
    # 关闭session:
    session.close()
    
new=User(name='w4ss')

insert(new)


