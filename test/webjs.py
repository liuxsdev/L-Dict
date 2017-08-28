# -*- coding: utf-8 -*- 

'''
    【简介】
    QWebView中网页调用JavaScript 
  
'''


from PyQt5.QtWidgets  import QApplication , QWidget , QVBoxLayout , QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
from PyQt5.QtCore import *

# 创建一个 application实例
app = QApplication(sys.argv)  
win = QWidget()
win.setWindowTitle('Web页面中的JavaScript与')

# 创建一个垂直布局器
layout = QVBoxLayout()
win.setLayout(layout)

# 创建一个 QWebEngineView 对象
view = QWebEngineView()
url=QFileInfo("index.html").absoluteFilePath()
view.load(QUrl(url))


# 创建一个按钮去调用 JavaScript代码
button = QPushButton('设置全名')

def js_callback(result):
    print(result)
    
def complete_name():
    js="setvm(%s)" % "{'basic': {'explains': ['n. 大小；尺寸']}}"
    view.page().runJavaScript(js, js_callback)

# 按钮连接 'complete_name'槽，当点击按钮是会触发信号
button.clicked.connect(complete_name)

# 把QWebView和button加载到layout布局中
layout.addWidget(view)
layout.addWidget(button)

# 显示窗口和运行app
win.show()
sys.exit(app.exec_())
