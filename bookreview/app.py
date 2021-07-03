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
@app.route('/review', methods=['POST'])
def write_review():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': '이 요청은 POST!'})


@app.route('/review', methods=['GET'])
def read_reviews():
    title_receive = request.args.get('title_give')
    author_receive = request.args.get('author_give')
    review_receive = request.args.get('review_give')

    #dictionary 생성
    doc = {
        'title':title_receive,
        'author':author_receive,
        'review':review_receive
    }

    #저장
    db.bookreview.insert_one(doc)

    return jsonify({'msg': '저장완료'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)