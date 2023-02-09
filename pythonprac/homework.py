import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
#DB password가 <>로 되어있는데 <>제거 후 패스워드 입력
client = MongoClient('mongodb+srv://sparta:test@cluster0.kmja9d6.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
num=0
for tr in trs:
    num+=1
    rank = tr.select_one('td.number').text.strip()[0:2]
    if(num<10):
        rank = tr.select_one('td.number').text.strip()[0:1]
    title = tr.select_one('td.info > a.title').text
    artist = tr.select_one('td.info > a.artist.ellipsis').text.strip()
    print(rank,title.strip(),artist)     

# 코딩 시작