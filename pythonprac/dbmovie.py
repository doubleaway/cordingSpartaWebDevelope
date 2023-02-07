
from pymongo import MongoClient
#DB password가 <>로 되어있는데 <>제거 후 패스워드 입력
client = MongoClient('mongodb+srv://sparta:test@cluster0.kmja9d6.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta




##old_content > table > tbody > tr:nth-child(4) > td.title > div
allList=list(db.movies.find({},{'_id':False}))
gabunaum =db.movies.find_one({'title':'가버나움'})['point']
for a in allList:
    if gabunaum==a['point']:
        print(a['title'])


db.movies.update_one({'title':'가버나움'},{'$set':{'point':0}})

