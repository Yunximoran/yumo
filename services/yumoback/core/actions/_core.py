import json
import requests


ENCODING = "utf-8"




class aigc:
    apiUrl = "https://api.siliconflow.cn/v1/chat/completions"
    headers = {
        "Authorization": "Bearer sk-evotgvphlyvrorfrlcwrlounwqkytauesvcfpbrbadivqicr",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "Qwen/QwQ-32B",
        "stream": True,
        "messages": []
    }
    def __init__(self):
        pass
    
    # @staticmethod
    async def answer(self, question: str):
        msg = {
            "role": "user",
            "content": question
        }
        self.payload['messages'].append(msg)

        resp = requests.post(
            self.apiUrl,
            json=self.payload,
            headers=self.headers,
            stream=True
        )

        for line in resp.iter_lines():
            if line:
                dline:str = line.decode(ENCODING)
                if dline.startswith("data:"):
                    data = dline[5:].strip()
                    if data == "[DONE]":
                        break

                    try:
                        answer = json.loads(data)
                        delta: dict = answer['choices'][0]['delta']
                        reasoning_content = delta.get("reasoning_content", "")
                        content = delta.get("content", "")

                        res = content if content else reasoning_content
                        yield res
                    except (KeyError, json.JSONDecodeError) as e:
                        print("ERROR")


# def answer(question: str):
#     payload["messages"][0]["content"] = question
#     resp = requests.post(
#         AI_BASE_URL, 
#         json=payload,
#         headers=headers,
#         stream=True
#     )
#     for line in resp.iter_lines():
#         if line:
#             decoded_line = line.decode(ENCODING)
#             if decoded_line.startswith("data:"):
#                 data = decoded_line[5:].strip()
#                 if data == "[DONE]":
#                     break

#                 try:
#                     data = json.loads(data)
#                     delta:dict = data['choices'][0]['delta']


#                     # 推理过程
#                     reasoning_content = delta.get("reasoning_content", "")
#                     content = delta.get("content", "")
                    
#                     # 结论输出
#                     # content = data['choices'][0]["delta"].get("content", "")
#                     yield reasoning_content if not content else content
#                 except (KeyError, json.JSONDecodeError) as e:
#                     pass
