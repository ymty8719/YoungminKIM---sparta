from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           
client = MongoClient('localhost', 27017)  
db = client.dbsparta                     

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/sell', methods=['POST'])
def sell_things():

    name = request.form['name']
    call = request.form['call'']
    number = request.form['number']
    house = request.form['house']
	# 2. DB에 정보 삽입하기
    db.books.insert_one({
        'name' : name,
        'call' : call,
        'number' : number,
        'house' : house,
    })
    #리뷰 내용을 추가하는 것
    return jsonify({'result': 'success', 'msg': '목록이 성공적으로 작성되었습니다.'})

@app.route('/sell', methods=['GET'])
def read_sell():
    sell_things = list(db.sells.find({},{'_id' : False})) 

    return jsonify({'result':'success', 'msg': '이 요청은 GET!', 'data' : sell-things})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
