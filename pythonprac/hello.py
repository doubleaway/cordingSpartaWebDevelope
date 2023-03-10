import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
#DB password가 <>로 되어있는데 <>제거 후 패스워드 입력
client = MongoClient('mongodb+srv://sparta:test@cluster0.kmja9d6.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

##old_content > table > tbody > tr:nth-child(2) > td.point
# #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
trs = soup.select('#old_content > table > tbody > tr')
for tr in trs:
    a =  tr.select_one('td.title > div > a')

    if a is not None:
        title = a.text
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        point = tr.select_one('td.point').text
        print(title,rank,point)
        doc={
            'title':title,
            'rank':rank,
            'point':point
        }
        db.movies.insert_one(doc)

# 코딩 시작