import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

##old_content > table > tbody > tr:nth-child(2) > td.point
# #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
trs = soup.select('#old_content > table > tbody > tr')
for tr in trs:
    title =  tr.select_one('td.title > div > a')
    rank = tr.select_one('td:nth-child(1) > img')
    point = tr.select_one('td.point')
    if a is not None:
        print(title)
        print(rank[alt])
        print(c.text)


# 코딩 시작