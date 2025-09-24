
import os
from openai import OpenAI
from IPython.display import Markdown, display
import requests
openai = OpenAI()
from dotenv import load_dotenv


load_dotenv(override=True)  # 自动读取 .env 文件
openai_api_key = os.getenv('OPENAI_API_KEY')
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:20]}")
else:
    print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")
    
    
if deepseek_api_key:
    print("DEEPSEEK API Key exists and begins {deepseek_api_key[:4]}")
else:
    print("DEEPSEEK API Key not set - please head to the troubleshooting guide in the setup folder")
    
    









# 循环等待输入

while True:
    user_input = input("Please input (input q or quit to exit): ")

    if user_input.lower() in ["q", "quit"]:
        print("We finish, Bye！")
        break

    # 在这里你可以对 user_input 做其他处理
    print(f"Your question is: {user_input}")
    messagesIn = [
        {"role": "system", "content": "Hello, OpenAI" },
        {"role": "user", "content": user_input}
    ]

    client = OpenAI(api_key=openai_api_key)

    response = client.chat.completions.create(
    model="gpt-4o-mini",   # 例如 gpt-4o-mini，支持 sk-proj- key
    messages= messagesIn
    
)
    answer = response.choices[0].message.content

    print("The answer from the Agent: ",answer )
   # expert.py
   


while False:
    user_input = input("请输入内容 (输入 q 或 quit 退出): ")

    if user_input.lower() in ["q", "quit"]:
        print("程序结束，再见！")
        break

    # 在这里你可以对 user_input 做其他处理
    print(f"你刚才输入的是: {user_input}")

    headers = {
    "Authorization": f"Bearer {deepseek_api_key}",
    "Content-Type": "application/json",
    }

    json_body = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        "stream": False,
    }

    response = requests.post("https://api.deepseek.com/chat/completions",
                            headers=headers,
                            json=json_body)

    print(response.status_code)
    print(response.json())