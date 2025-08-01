import json
import requests

# 导入类型校验
from requests import Response

from lib import resolver

ENCODING = resolver("default", 'encoding')

class aigcore:
    __config = resolver("services", "django", "modules", "aigcore")

    # ===== 导入默认配置 ===== 
    # 基础配置模板
    __baseURL = __config.search("baseurl").data

    # 请求头模板
    __headers = {
        "Authorization": "Bearer sk-evotgvphlyvrorfrlcwrlounwqkytauesvcfpbrbadivqicr",
        "Content-Type": "application/json"
    }

    # 请求配置模板
    __payload = {
        "model": __config.search("model").data, 
        "stream": __config.search("stream").data,
        "messages": []
    }

    def __init__(self):
        self.dialogues = {}

    def get_dialugue(self):                     # 获取对话记录
        pass

    async def answer(self, question: str):      # 回答提问
        self.__payload['messages'].append({
            "role": "user",
            "content": question
        })

        resp = requests.post(
            self.__baseURL,
            stream=True,
            json=self.__payload,
            headers=self.__headers,
        )

        return await self.__reading(resp)
    
    
    
    def __create_new_dialogue(self):            # 创建 新对话(new dialogue) 模板
        playload = self.__payload.copy()
        return playload
    
    async def __reading(self, resp: Response):  # 解析响应流
        for line in resp.iter_lines():
            if line and isinstance(line, bytes):
                data:str = line.decode(ENCODING)

                # 校验数据类型
                if data.startswith("data:"):
                    # 读取数据文本
                    chunk = data[5:].strip()
                    
                    # 终止符，回答已完成
                    if chunk == "[DONE]":
                        break

                    try:
                        # 序列化数据对象
                        answer = json.loads(chunk)
                        delta: dict = answer['choices'][0]['delta']
                        reasoning_content = delta.get("reasoning_content", "")
                        content = delta.get("content", "")

                        yield content if content else reasoning_content
                    except (KeyError, json.JSONDecodeError) as e:
                        print("ERROR")
                    except Exception as e:
                        print(e)
            else:
                continue


if __name__ == '__main__':
    aigcore = aigcore()
