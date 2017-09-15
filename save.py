# -*-coding:utf-8 -*-
from youdao import getYoudao
import sqlite3
import time

conn=sqlite3.connect('./Dict/test.db')
cu=conn.cursor()

sql_createTable='CREATE TABLE IF NOT EXISTS word(id integer PRIMARY KEY AUTOINCREMENT,name text UNIQUE,explains text,initials text,addtime text,searchtimes text,groups text)'

cu.execute(sql_createTable)



def insert_toDB(name=None,explains=None,initials=None,addtime=None,searchtimes=None,groups=None):
    addtime=str(time.time())   #添加时间
    initials=name[0].capitalize()  #首字母
    sql="INSERT INTO word(name,explains,initials,addtime,searchtimes,groups) VALUES (?,?,?,?,?,?)"
    try:
        cu.execute(sql,(name,explains,initials,addtime,searchtimes,groups))
    except sqlite3.IntegrityError as e:
        print(e,'exists!')
def query_inDB(word):
    SQL="SELECT name,explains from word WHERE name='%s'" % word
    cu.execute(SQL)
    res=cu.fetchall()
    print(res)


query_inDB('go')
cu.close()
conn.commit()