import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests                        # 파이썬으로 웹페이지 연결
from bs4 import BeautifulSoup as bs    # 분석을 용이하게 정제


form_class = uic.loadUiType("musicapp.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# 단추 인식 시키기
        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):

        response = requests.get('https://music.bugs.co.kr/chart')
        soup = bs(response.text)
        
        rank = 1

        for i in range(100):
            title = soup.select('p.title > a')[i].text
            singer = soup.select('p.artist > a')[i].text

            self.tableWidget.setItem(i, 0, QTableWidgetItem("Bugs"))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(rank)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(title))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(singer))

            rank += 1




app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()


# 윈도우 실행파일 만들기    pyinstaller --noconsole --onefile musicapp.py
