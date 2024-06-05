

import time
from zhipuai import ZhipuAI

client = ZhipuAI(api_key="6918fa714338f6e35e9cccce10d9d7cb.ln6PCFJRWKpcoCfI")  # 请填写您自己的APIKey

while True:
    user_input = input("请输入您的问题：")
    response = client.chat.asyncCompletions.create(
        model="chatglm_turbo",  # 填写需要调用的模型名称
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ],
    )
    task_id = response.id
    task_status = ''
    get_cnt = 0

    while task_status != 'SUCCESS' and task_status != 'FAILED' and get_cnt <= 40:
        result_response = client.chat.asyncCompletions.retrieve_completion_result(id=task_id)
        task_status = result_response.task_status

        if task_status == 'SUCCESS':
            print("回复：", result_response.message)

        time.sleep(2)
        get_cnt += 1
