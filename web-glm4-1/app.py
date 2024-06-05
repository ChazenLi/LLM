from flask import Flask, request, jsonify, render_template, send_from_directory
import requests
import jwt
import time

app = Flask(__name__, static_folder='static')  # 静态文件夹路径

api_key = '87882731ca8f0329e445e0270db8cb50'
api_secret = 'V5MK4aVEmwQDlqPk'


def generate_jwt(api_key, api_secret):
    payload = {
        "sub": api_key,  # 和AI平台的文档一致使用sub作为subject的缩写
        "exp": int(time.time()) + 3600  # 过期时间设置为1小时后
    }
    token = jwt.encode(payload, api_secret, algorithm="HS256")
    return "Bearer " + token  # 添加"Bearer "前缀以符合认证格式


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']
    token = generate_jwt(api_key, api_secret)

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    payload = {
        'input': {
            'question': question,
            'other_parameters': '...'  # 根据具体API调整参数
        }
    }

    try:
        response = requests.post('API_ENDPOINT', headers=headers, json=payload)  # 改为你的API端点
        response.raise_for_status()
        answer = response.json().get('answer', '未获取到答案')
    except requests.HTTPError as http_err:
        answer = f'HTTP error occurred: {http_err}'
    except Exception as err:
        answer = f'Other error occurred: {err}'

    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run(debug=True)