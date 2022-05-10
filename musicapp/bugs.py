#  벅스
import requests                        # 파이썬으로 웹페이지 연결
from bs4 import BeautifulSoup as bs    # 분석을 용이하게 정제
import pandas as pd                    # 데이터 분석 (엑셀로 저장, 데이터프레임)

response = requests.get('https://music.bugs.co.kr/chart')
soup = bs(response.text)
song_data = []
rank = 1

songs = soup.select('table.byChart > tbody > tr')

for song in songs:
  title = song.select('p.title > a')[0].text
  singer = song.select('p.artist > a')[0].text
  song_data.append(['Bugs', rank, title, singer])
  rank += 1

df = pd.DataFrame(song_data, columns = ['차트명','순위','타이틀','가수'])

print(df)


# 윈도우 실행파일 만들기    pyinstaller --noconsole --onefile musicapp.py