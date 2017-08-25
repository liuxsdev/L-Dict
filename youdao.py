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

def genHTML(word):
    data=getYoudao(word)
    str_data=str(json.dumps(data,ensure_ascii=False)).replace('"',"'") #in js json can't use single '?? 
    # can html be inline?
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
    return html


if __name__ == '__main__':
    #a=getYoudao('sys')
    #print(a,type(a))
    #printYoudao(a)
    b=genHTML('sys')
    print(b)
