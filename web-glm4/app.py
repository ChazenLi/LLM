from flask import Flask, request, jsonify, render_template, send_from_directory
import requests
import jwt
import time

app = Flask(__name__)

# 请确保将这些值替换为您的实际API Key和Secret部分
api_key = '87882731ca8f0329e445e0270db8cb50'
api_secret = 'V5MK4aVEmwQDlqPk'

def generate_jwt(api_key_id, api_secret):
    payload = {
        "api_key": api_key_id,
        "exp": int(time.time()) + 3600,  # 设置为1小时后过期
        "timestamp": int(time.time()),
    }
    token = jwt.encode(payload, api_secret, algorithm="HS256",
                       headers={"alg": "HS256", "sign_type": "SIGN"})
    return token


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('static', path)

@app.route('/api/chat', methods=['POST'])
def chat():
    # 从请求中获取问题
    data = request.json
    messages = data['messages']
    api_key = data['api_key']
    api_secret = data['api_secret']

    # 生成JWT
    token = generate_jwt(api_key, api_secret)

    # 构造请求参数
    payload = {
        'model': 'glm-4',  # 替换为要调用的模型名称
        'messages': messages,
        # 此处添加其他必需的参数，例如do_sample, temperature, top_p等
    }

    # 设置请求头，使用JWT进行鉴权
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }

    # 发起POST请求到智谱AI API
    response = requests.post(
        'https://open.bigmodel.cn/api/paas/v4/chat/completions',
        json=payload,
        headers=headers
    )

    # 处理响应
    if response.status_code == 200:
        responseData = response.json()
        if 'choices' in responseData:
            answer = responseData['choices'][0]["message"]['content']
            return jsonify({'success': True, 'message': "", 'answer': answer})
        else:
            return jsonify({'success': False, 'message': "请求失败，未找到响应"})
    else:
        return jsonify({'success': False, 'message': "请求失败，请检查API密钥和API URL"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
