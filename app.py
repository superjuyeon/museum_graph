import json
from flask import Flask, render_template, request, url_for, redirect, session
import logging

app = Flask(__name__, static_url_path='/static')


app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.html')

	
if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
    app.run(host='0.0.0.0', port=8889, debug=True, threaded=True)
    # app.run(host='192.168.0.22', port=8889, debug=True, threaded=True)  # PC와 tablet이 같은 wifi를 사용해야함