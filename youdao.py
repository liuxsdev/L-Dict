# -*-coding:utf-8 -*-
import json
import requests


def getYoudao(kw):
    url='http://fanyi.youdao.com/openapi.do?keyfrom=dictquery&key=947851566&type=data&doctype=json&version=1.1&q='+kw
    r=requests.get(url)
    res=r.json()
    word={}
    word['query']=res['query']
    word['translation']=res['translation']
    word['explains']=res.get('basic',{'explains':''}).get('explains')
    word['web']=res.get('web',[])
    word['phonetic']=res.get('basic',{}).get('phonetic',"c") or ''
    return word



def printYoudao(s):
    print('\033[97m{}\033[0m'.format(s['query']))      #show the search word
    if 'phonetic' in s['phonetic']:
        phonetic=s['phonetic']  #如果有发音，则显示
        print(phonetic)
    print("\033[1;35m[释义]\033[0m")
    if 'translation' in s:
        trans=s['translation']
        for i in trans:
            print(i)
    print("\033[1;35m[详解]\033[0m")
    if 'explains' in s:
        explains=s['explains']
        for i in explains:
            print(i)
    print('\033[1;35m[网络释义]\033[0m')
    if 'web' in s:
        for i in s['web']:
            print(i['key'],'\t',';'.join(i['value']))



if __name__ == '__main__':
    a=getYoudao('aromatic surface')
    printYoudao(a)
    #b=genHTML('good')
    #print(b)