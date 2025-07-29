import requests

url = "https://api.siliconflow.cn/v1/chat/completions"

payload = {
    "model": "Qwen/QwQ-32B",
    "messages": [
        {
            "role": "user",
            "content": "What opportunities and challenges will the Chinese large model industry face in 2025?"
        }
    ]
}
headers = {
    "Authorization": "Bearer sk-evotgvphlyvrorfrlcwrlounwqkytauesvcfpbrbadivqicr",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
if __name__ == '__main__':
    pass
    # yumoback.startup([sys.argv[0], "runserver"])
    # yumoback.startasgi(
    #     "localhost",
    #     8000,
    #     True
    # )
