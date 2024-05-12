import json
import pandas as pd

with open('../yumo.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(data)


def ldf(data, frameList=[]):
    for nextElem in data.values():
        if isinstance(nextElem, dict):
            ldf(nextElem, frameList)
        else:
            frameList.append(frameList)

    return frameList


frameList = ldf(data)
for frame in frameList:
    print(frame)
