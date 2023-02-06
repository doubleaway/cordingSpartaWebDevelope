from pymongo import MongoClient
#DB password가 <>로 되어있는데 <>제거 후 패스워드 입력
client = MongoClient('mongodb+srv://sparta:test@cluster0.kmja9d6.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

#doc={'name':"철수","age":22}
#db.users.insert_one(doc)
#doc={'name':"영희","age":32}
#db.users.insert_one(doc)
#doc={'name':"수영","age":27}
#db.users.insert_one(doc)
#실행 후 browser collections눌러서 실행

#전부 찾아오기
all_users = list(db.users.find({},{'_id':False}))
for a in all_users:
    print(a)

#하나만 가져오기
user=db.users.find_one({})
print(user)

#이름이 영수인 값을 찾아서 나이를 55로 바꿔라
db.users.update_one({'name':'철수'},{'$set':{'age':55}})

#삭제 철수란 이름을 가진 값을 하나 삭제해라
db.users.delete_one({'name':'철수'})

#알게 된점! _one은 메소드는 맨 나중에 저장된 값을 조작하는듯함

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})