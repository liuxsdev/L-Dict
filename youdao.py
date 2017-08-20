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
    print('[{}]'.format(s['word']))      #show the search word
    if 'basic' in s:
        if 'phonetic' in s['basic']:
            phonetic=s['basic']['phonetic']  #如果有发音，则显示
            print(phonetic)
        print("释义:")
        if 'translation' in s:
        	    trans=s['translation']
        	    for i in trans:
        	        print(i)
        	if 'explains' in s['basic']:
        	    explains=s['basic']['explains']
            for i in explains:
                print(i)
    else:
        print('无释义')

if __name__ == '__main__':
    a=getYoudao('sys')
    #print(a,type(a))
    printYoudao(a)
