from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is watash Home!'

@app.route('/mypage')
def mypage():
   return '<button>HoHoHo</button>'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)