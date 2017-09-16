#-*- coding:utf-8 -*-
import requests
import json
from pprint import pprint
import sqlite3
class Youdao(object):
    def getYoudaoAPI(self,word):
        url='http://fanyi.youdao.com/openapi.do?keyfrom=dictquery&key=947851566&type=data&doctype=json&version=1.1&q='+word
        r=requests.get(url)
        res=r.json()
        word={}
        word['query']=res['query']
        word['translation']=res['translation']
        word['explains']=res.get('basic',{'explains':[]}).get('explains')
        word['web']=res.get('web',[])
        word['phonetic']=res.get('basic',{}).get('phonetic',"") or ''
        return word
    
class DB(object):
    def __init__(self):
        self.conn=sqlite3.connect('./dict/test.db')
        self.cu=self.conn.cursor()
    def query(self,word):
        SQL="SELECT * from word WHERE name='%s'" % word
        self.cu.execute(SQL)
        res=self.cu.fetchall()[0]
        return res   
    def __del__(self):
        self.cu.close()
        self.conn.commit()
        print('class del')
    
#a=Youdao()
#pprint(a.getYoudaoAPI('go'))
b=DB()
a=b.query('go')
print(a[2])


