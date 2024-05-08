from lib.syskit import parseArgs, logger    # 在__init__中导入的模块，在__init__被其他文件调用是也会一同导入
from lib.build import makedir
# 可以实现 import package 后 使用当中所有方法而不是，使用from package import modules

import requests

args = parseArgs()
logger = logger("demo")

try:
    URL = args['URL']
except KeyError:
    URL = ['https://www.baidu.com']

print(URL)
file = ['Home', 'Fanyi']
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                  "537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}
for url, f in zip(URL, file):
    resp = requests.get("https://www.baidu.com", headers=headers)
    resp.encoding = 'utf-8'

    dumpPath = "source"
    makedir(dumpPath)

    with open(f"{dumpPath}\\{f}.html", 'w', encoding='utf-8') as fp:
        fp.write(resp.text)

# s1 = "URL=[https://demo1, https://demo2]"
#
# match_search = re.search('=+', s1)  # return re.Match * span[记录搜索目标在字符串中的起始位置]  # 匹配失败时返回 None
# match_findall = re.findall('=', s1)  # return list * 返回所有配置对象                        # 匹配失败时返回 []
#
# s = match_search.start()
# e = match_search.end()
# print(match_search)
# print(match_search.start())
# print(match_search.end())
# print("[3]", s1[3])  # 两种切片方法得到的结果是一样的
# print("[3: 4]", s1[3:4])
#
# print("front", s1[:s])
# print("rear", s1[e:])
#
# match_err = re.findall("214214", s1)
# print(match_err)
#
# valMatch = re.findall(r'[^\[\], ]+', s1[e:])
# print(valMatch)
