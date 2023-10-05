import json
import requests
import asyncio
import websockets

class OverseesFuturesCls:
    # 업종기간별추이
    def oversees_futures_master_inquiry(self, ACCESS_TOKEN):
        # 요청 url
        PATH = "overseas-futureoption/market-data"
        URL = f"{self.BASE_URL}/{PATH}"

        # 요청 header
        header = {
            "content-type":"application/json; charset=utf-8",
            "authorization": f"Bearer {ACCESS_TOKEN}",
            "tr_cd":"o3101",
            "tr_cont":"N",
            "tr_cont_key":"",
        }

        # body
        body = {
              "o3101InBlock": {
                "gubun": ""
              }
            }

        # 요청 보내기
        request = requests.post(URL, headers=header, data=json.dumps(body))
        result = request.json()
        print(result)
        return result