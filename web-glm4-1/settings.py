# settings.py

# settings.py

# 直接硬编码API密钥和API URL
API_KEY = '87882731ca8f0329e445e0270db8cb50.V5MK4aVEmwQDlqPk'
API_URL = 'https://open.bigmodel.cn/api/paas/v4/chat/completions'
MODEL_NAME = 'glm-4'  # 示例使用的模型名称
DEBUG = True  # 开发模式开启

# 使用环境变量获取API密钥的代码被注释掉，留作备用
# import os
# API_KEY = os.environ.get('ZHIPUAI_API_KEY', 'your-default-api-key')
# API_URL = os.environ.get('ZHIPUAI_API_URL', 'https://open.bigmodel.cn/api/paas/v4/chat/completions')

# 可根据需要添加其他配置