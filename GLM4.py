import time
from zhipuai import ZhipuAI

client = ZhipuAI(api_key="87882731ca8f0329e445e0270db8cb50.V5MK4aVEmwQDlqPk")  # 请填写您自己的APIKey

response = client.chat.asyncCompletions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=[
        {
            "role": "user",
            "content": "我想知道有哪些描述扩散的数学模型，例如一个球壳，内部有酸性溶液，质子浓度为a，球壳上有一个孔，能够允许球壳内部溶液渗出，球壳外是质子浓度为b的溶液，以球壳表面一点为坐标系原点O，球壳外一点到球壳表面这一点的距离为x；质子浓度为y；使用何种数学函数进行描述？请返回适当数学函数描述"
        }
    ],
)
task_id = response.id
task_status = ''
get_cnt = 0

while task_status != 'SUCCESS' and task_status != 'FAILED' and get_cnt <= 40:
    result_response = client.chat.asyncCompletions.retrieve_completion_result(id=task_id)
    print(result_response)
    task_status = result_response.task_status

    time.sleep(2)
    get_cnt += 1
