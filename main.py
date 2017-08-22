
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow
from PyQt5.QtGui import QClipboard
from PyQt5.QtCore import Qt
from youdao import getYoudao,printYoudao
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtCore import QUrl


class MianWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.initUI()
        self.addClipbordListener()

    def initUI(self,html):   
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')   
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.browser = QWebView()
        url = 'file:///H:/workspace/web/app/Dict/index.html'
        #self.browser.setUrl(QUrl(url))
        self.browser.setHtml(html)
        self.setCentralWidget(self.browser)
        self.show()


    def addClipbordListener(self):
        clipboard = QApplication.clipboard()
        clipboard.dataChanged.connect(self.onClipboradChanged)

    def onClipboradChanged(self):
        clipboard = QApplication.clipboard()
        printYoudao(getYoudao(clipboard.text()))
        self.initUI(str(getYoudao(clipboard.text())))
        # self.browser = QWebView()
        # url = 'file:///H:/workspace/web/app/Dict/index.html'
        # # 指定打开界面的 URL
        # self.browser.setUrl(QUrl(url))
        # self.browser.setHtml('ds')
        # self.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MianWindow()
    sys.exit(app.exec_())


