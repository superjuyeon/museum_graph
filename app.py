import json
from flask import Flask, render_template, request, url_for, redirect, session
import logging
from flask_fontawesome import FontAwesome
import os

basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'static/datasets/배재_단어.json')
a_json = open(data_file, encoding = 'utf-8')
new_dict = json.load(a_json)


app = Flask(__name__, static_url_path='/static')
fa = FontAwesome(app)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.html')

@app.route('/d2', methods=['GET', 'POST'])
def d2():
    return render_template('d2.html')

@app.route('/d4', methods=['GET', 'POST'])
def d4():
    return render_template('d4.html')

@app.route('/d5', methods=['GET', 'POST'])
def d5():
    return render_template('d5.html')

@app.route('/d7', methods=['GET', 'POST'])
def d7():
    return render_template('d7.html')

@app.route('/d8', methods=['GET', 'POST'])
def d8():
    return render_template('d8.html')

@app.route('/d9', methods=['GET', 'POST'])
def d9():
    return render_template('d9.html')

@app.route('/d10', methods=['GET', 'POST'])
def d10():
    return render_template('d10.html')

@app.route('/get_answer', methods=['GET', 'POST'])
def get_answer():
    if request.method == 'POST':
        question = request.form['question_id']

        answer = new_dict[question]
        return answer

if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
    app.run(host='0.0.0.0', port=8889, debug=True, threaded=True)
    # app.run(host='192.168.0.22', port=8889, debug=True, threaded=True)  # PC와 tablet이 같은 wifi를 사용해야함