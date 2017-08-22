
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow
from PyQt5.QtGui import QClipboard
from PyQt5.QtCore import Qt,QUrl
from PyQt5.QtWebKitWidgets import QWebView
from youdao import getYoudao,printYoudao

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.addClipbordListener()

    def initUI(self):   
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')   
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()


    def addClipbordListener(self):
        clipboard = QApplication.clipboard()
        clipboard.dataChanged.connect(self.onClipboradChanged)

    def onClipboradChanged(self):
        clipboard = QApplication.clipboard()
        a=getYoudao(clipboard.text())
        printYoudao(a)
        self.show = showWin(str(a))
        self.show.show()



class showWin(QMainWindow):
    def __init__(self,n):
        self.n=n
        super(showWin, self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(280,600)
        self.browser = QWebView()
        #url = 'file:///H:/workspace/web/app/Dict/index.html'
        #self.browser.setUrl(QUrl(url))
        self.browser.setHtml(self.n)
        self.setCentralWidget(self.browser)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


