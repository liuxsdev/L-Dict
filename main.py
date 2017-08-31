
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QPushButton
from PyQt5.QtGui import QClipboard
from PyQt5.QtCore import Qt,QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from youdao import getYoudao,printYoudao,genHTML


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
        word=clipboard.text()
        a=getYoudao(word)
        printYoudao(a)
        js="vm.youdao=%s" % str(getYoudao(word))
        print(js)
        self.show = showWin(js)
        self.show.show()



class showWin(QMainWindow):
    def __init__(self,js):
        self.js=js
        super(showWin, self).__init__()
        self.initUI()
    def initUI(self):
        #self.setWindowOpacity(0.7)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(650,230)
        self.browser = QWebEngineView()
        url = 'H:/workspace/git/L-Dict/test/index.html'
        self.browser.load(QUrl(url))
        self.browser.loadFinished.connect(self.runjs)
        self.setCentralWidget(self.browser)
    def runjs(self):
        self.browser.page().runJavaScript(self.js)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


