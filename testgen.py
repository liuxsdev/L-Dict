#-*- coding:utf-8 -*-




'''
var data={
	'translation': ['微笑'], 
	'basic': {
		'us-phonetic': 'smaɪl',
		'phonetic': 'smaɪl', 
		'uk-phonetic': 'smaɪl', 
		'explains': ['n. 微笑；笑容；喜色', 'vt. 微笑着表示', 'vi. 微笑', 'n. (Smile)人名；(塞)斯米莱']
	}, 
	'query': 'smile', 
	'errorCode': 0, 
	'web': [{'value': ['微笑', '贾乃亮', 'Smile (布赖恩·威尔逊专辑)'], 'key': 'Smile'}, {'value': ['再次微笑', '笑吧！东海', '再次微笑'], 'key': 'Smile Again'}, {'value': ['微笑宝贝', '和我一起来唱逍遥歌', '微笑宝宝'], 'key': 'Smile Baby'}], 
	'word': 'smile'
};
var data2={
	'translation': ['sys'], 
	'basic': {
		'explains': ['abbr. 系统文件（计算机文件扩展名）', 'n. (Sys)人名；(捷)西斯']
	}, 
	'query': 'SYS', 
	'errorCode': 0, 
	'web': [{'value': ['制式', '多制式系统', '系统文件'], 'key': 'SYS'}, {'value': ['中频设定'], 'key': 'VIF SYS'}, {'value': ['系统优化精灵', '系统优化软件', '免费系统优化'], 'key': 'Sys Optimizer'}], 
	'word': 'sys'
};
'''
import json
data={
	'translation': ['sys'], 
	'basic': {
		'explains': ['abbr. 系统文件（计算机文件扩展名）', 'n. (Sys)人名；(捷)西斯']
	}, 
	'query': 'SYS', 
	'errorCode': 0, 
	'web': [{'value': ['制式', '多制式系统', '系统文件'], 'key': 'SYS'}, {'value': ['中频设定'], 'key': 'VIF SYS'}, {'value': ['系统优化精灵', '系统优化软件', '免费系统优化'], 'key': 'Sys Optimizer'}], 
	'word': 'sys'
}

str_data=str(json.dumps(data,ensure_ascii=False)).replace('"',"'")

html='''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
    <title></title>
<style>
	  body{background-color:black;color:white}
	  li {list-style-type:none;}
</style>
  </head>
  <body>
    <div id="word"></div>
	<div id="phonetic"></div>
	<div id="explains"></div>
	<div id="web"></div>
<script>
var data=%s
var word=document.getElementById("word");
var phonetic=document.getElementById("phonetic");
var explains=document.getElementById("explains");
var web=document.getElementById("web");
function gen(data){
	word.innerHTML = data.word;
	str_li = '';
	if (data.basic.explains.length == 0)
	{
		explains.innerHTML = "<p>No result</p>";
	}
	else
	{
		for (var i=0;i < data.basic.explains.length;i++)
		{
			str_li += "<p>" + data.basic.explains[i] + "</p>";
		}
		explains.innerHTML = str_li;
	}
}
gen(data);
</script>
  </body>
</html>
''' % str_data

print(html)




#SQLAlchemy TEST

# 导入: 
from sqlalchemy import Column, String, create_engine ,Integer
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base 
# 创建对象的基类: 
Base = declarative_base() 
# 定义User对象: 
class User(Base): 
    # 表的名字: 
    __tablename__ = 'user' 
    # 表的结构: 
    idd= Column(Integer, primary_key=True) 
    name = Column(String(20)) 
    def __init__(self,idd,name):
        self.idd=idd
        self.name=name
    
# 初始化数据库连接: engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test') # 创建DBSession类型: DBSession = sessionmaker(bind=engine) 


engine=create_engine('sqlite:///test.db')
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(5,'Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()


