import requests, json

url = "https://api.siliconflow.cn/v1/chat/completions"

payload = {
    "model": "Qwen/QwQ-32B",
    "stream": True,
    "messages": [
        {
            "role": "user",
            "content": "conda虚拟环境怎么使用"
        }
    ]
}
headers = {
    "Authorization": "Bearer sk-evotgvphlyvrorfrlcwrlounwqkytauesvcfpbrbadivqicr",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers, stream=True)

reasoning = True
full_response = ""
for line in response.iter_lines():
    if line:
        decode_line = line.decode("utf-8")
        if decode_line.startswith("data:"):
            data_str = decode_line[5:].strip()
            if data_str == "[DONE]":
                break

            try:
                data = json.loads(data_str)
                reasoning_content = data['choices'][0]["delta"].get("reasoning_content", "")

                content = data['choices'][0]["delta"].get("content", "")
                
                if content:
                    full_response += content
                elif reasoning_content:
                    full_response += reasoning_content
                    
            except (KeyError, json.JSONDecodeError) as e:
                print(f"\n[解析错误] {e} | 原始数据: {decode_line}")

print("\n\n完整回复")
print(full_response)
# data = response.json()
# msg = data['choices'][0]['message']['content']
# print(msg)
if __name__ == '__main__':
    pass
