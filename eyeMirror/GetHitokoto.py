import json
import requests

class GetHitokoto:

    @staticmethod
    def get():
        __url = 'https://v2.jinrishici.com/sentence'
        __headers = {'X-User-Token': 'RgU1rBKtLym/MhhYIXs42WNoqLyZeXY3EkAcDNrcfKkzj8ILIsAP1Hx0NGhdOO1I'}
        __return = requests.get(__url, headers=__headers)
        __data = json.loads(__return.text)
        return __data["data"]["content"] + ' ' + __data["data"]["origin"]["title"]
