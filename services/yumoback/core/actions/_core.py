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
                        if res: yield res
                    except (KeyError, json.JSONDecodeError) as e:
                        print("ERROR")
                    except Exception as e:
                        print(e)

