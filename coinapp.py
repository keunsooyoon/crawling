import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pybithumb

tickers = ['BTC','ETH','XRP','ADA','BCH']

form_class = uic.loadUiType("coin5.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# 단추 인식 시키기
        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        for i, ticker in enumerate(tickers):
            price = pybithumb.get_current_price(ticker)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(ticker))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
 
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()

# 윈도우 실행파일 만들기    pyinstaller --noconsole --onefile coin5.py
