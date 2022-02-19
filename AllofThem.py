import sys # 시스템 접근
from PyQt5.QtWidgets import *
from PyQt5 import uic              # pyqt 사용 라이브러리
from selenium import webdriver # 브라우저 컨트롤
from bs4 import BeautifulSoup as bs # 브라우저 정제

driver = webdriver.Chrome('chromedriver.exe')


form_class = uic.loadUiType("music_chart.ui")[0] # pyqt 만들어온 창 열기

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry1)
        self.pushButton_2.clicked.connect(self.inquiry2)
        self.pushButton_3.clicked.connect(self.inquiry3)
    
    def inquiry1(self):
        url1 = "https://www.melon.com/chart/"
        driver.get(url1)
        html = driver.page_source
        soup = bs(html)
        songs = soup.select('div.wrap_song_info')
        rank = 1
        for i in range(100):
            singer = soup.select('div.wrap_song_info > div.rank02 > a')[i].text
            title = soup.select('div.wrap_song_info > div.rank01 > span > a')[i].text
            self.tableWidget.setItem(i, 0, QTableWidgetItem("Melon"))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(rank)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(title))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(singer))
            rank += 1
    
    def inquiry2(self):
        url2 = "https://www.genie.co.kr/chart/top200?ditc=D&rtm=N"
        driver.get(url2)
        html = driver.page_source
        soup = bs(html)
        rank = 1
        for i in range(50):
            singer = soup.select('tbody > tr.list > td.info > a.artist')[i].text
            title = soup.select('tbody > tr.list > td.info > a.title')[i].text
            title = title.replace('\n', "")
            title = title.replace('  ', "")
            self.tableWidget.setItem(i, 0, QTableWidgetItem("Geine"))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(rank)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(title))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(singer))
            rank += 1
            if rank >= 51:
                url2 = "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20220117&hh=00&rtm=N&pg=2"
                driver.get(url2)
                html = driver.page_source
                soup = bs(html)
                for i in range(50):
                    singer = soup.select('tbody > tr.list > td.info > a.artist')[i].text
                    title = soup.select('tbody > tr.list > td.info > a.title')[i].text
                    title = title.replace('\n', "")
                    title = title.replace('  ', "")
                    self.tableWidget.setItem(i+50, 0, QTableWidgetItem("Geine"))
                    self.tableWidget.setItem(i+50, 1, QTableWidgetItem(str(rank)))
                    self.tableWidget.setItem(i+50, 2, QTableWidgetItem(title))
                    self.tableWidget.setItem(i+50, 3, QTableWidgetItem(singer))
                    rank += 1
            


    def inquiry3(self):
        url3 = "https://music.bugs.co.kr/chart?wl_ref=M_left_02_01"
        driver.get(url3)
        html = driver.page_source
        soup = bs(html)
        songs = soup.select('table.byChart > tbody > tr')
        rank = 1
        i = 0
        for song in songs:
            title = song.select('p.title > a')[0].text
            singer = song.select('p.artist > a')[0].text
            self.tableWidget.setItem(i, 0, QTableWidgetItem("Bugs"))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(rank)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(title))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(singer))
            rank += 1
            i += 1
        
        
app = QApplication(sys.argv)
window = MyWindow()  # 객체생성
window.show()        # 객체로 창 띄우기
app.exec_()          # 창을 계속 유지
