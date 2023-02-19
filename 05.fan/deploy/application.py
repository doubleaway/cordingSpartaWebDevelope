from flask import Flask, render_template, request, jsonify
application = app = Flask(__name__)
from pymongo import MongoClient
#DB password가 <>로 되어있는데 <>제거 후 패스워드 입력
client = MongoClient('mongodb+srv://sparta:test@cluster0.kmja9d6.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_recieve = request.form['name_give']
    comment_receive=request.form['comment_give']
    doc={
        'name':name_recieve,
        'comment':comment_receive
    }
    db.fans.insert_one(doc)

    return jsonify({'msg': '저장 완료'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_comment = list(db.fans.find({},{'_id':False}))

    return jsonify({'result': all_comment})

if __name__ == '__main__':
    app.run()