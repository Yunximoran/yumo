from lib import Resolver
from pathlib import Path

import requests


CONFIGPATH = Path(__file__).parent / Path(".config")

class TestUrl:
    _conf = Resolver(CONFIGPATH)
    BaseUrl = _conf("base-url")
    def __init__(self):
        pass


    def test_get_hello(self):
        resp = requests.get(self.BaseUrl + '/hello', params={
            "param_1": 2005,
            "param_2": "world"
        })
        return resp