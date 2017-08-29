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


# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(name='w3')
# 添加到session:
session.merge(new_user)
#session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()