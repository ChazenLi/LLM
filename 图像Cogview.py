from zhipuai import ZhipuAI
client = ZhipuAI(api_key="6918fa714338f6e35e9cccce10d9d7cb.ln6PCFJRWKpcoCfI") # 请填写您自己的APIKey

response = client.images.generations(
    model="cogview-3", #填写需要调用的模型名称
    prompt="、二次元、短发",
)
print(response.data[0].url)