# -*-coding:utf-8 -*-
import json
import requests


def getYoudao(kw):
    url='http://fanyi.youdao.com/openapi.do?keyfrom=dictquery&key=947851566&type=data&doctype=json&version=1.1&q='+kw
    r=requests.get(url)
    res=r.json()
    res['word']=kw
    return res



def printYoudao(s):
    phonetic=s['basic']['phonetic']
    trans=s['translation']
    explains=s['basic']['explains']
    print('[{}]'.format(s['word']))
    #print(phonetic)
    # for i in trans:
    #     print(i)
    print("释义:")
    for i in explains:
        print(i)

if __name__ == '__main__':
    a=getYoudao('good')
    print(a,type(a))
    printYoudao(a)
