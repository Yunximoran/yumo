import requests

AI_BASE_URL = "https://api.siliconflow.cn/v1/chat/completions"

payload = {
    "model": "Qwen/QwQ-32B",
    "messages": [
        {
            "role": "user",
            "content": None # 提问占位符号
        }
    ]
}

headers = {
    "Authorization": "Bearer sk-evotgvphlyvrorfrlcwrlounwqkytauesvcfpbrbadivqicr",
    "Content-Type": "application/json"
}
def answer(question: str):
    payload["messages"]["content"] = question
    resp = requests.post(AI_BASE_URL, json=payload, headers=headers)
    return resp.json()