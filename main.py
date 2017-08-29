
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
        self.show = showWin(genHTML(word))
        self.show.show()



class showWin(QMainWindow):
    def __init__(self,n):
        self.n=n
        super(showWin, self).__init__()
        self.initUI()
    def initUI(self):
        #self.setWindowOpacity(0.7)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(650,230)
        self.browser = QWebEngineView()
        # url = 'H:/workspace/git/L-Dict/test/index.html'
        # self.browser.load(QUrl(url))
        self.browser.setHtml(self.n)
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


