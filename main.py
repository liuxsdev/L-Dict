
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QClipboard
from youdao import getYoudao

class MianWindow(QWidget):
    def __init__(self):
        super().__init__()
        #self.initUI()
        self.addClipbordListener()

    def initUI(self):   
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')   
        # self.show()

    def addClipbordListener(self):
        clipboard = QApplication.clipboard()
        clipboard.dataChanged.connect(self.onClipboradChanged)

    def onClipboradChanged(self):
        clipboard = QApplication.clipboard()
        print(getYoudao(clipboard.text()))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MianWindow()
    sys.exit(app.exec_())


