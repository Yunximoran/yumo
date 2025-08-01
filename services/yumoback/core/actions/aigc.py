import json
import requests
from ...aigctool import aigcore

# 创建全局AIGC核心模块
aigcore = aigcore()

async def answer(question:str):
    return await aigcore.answer(question)
