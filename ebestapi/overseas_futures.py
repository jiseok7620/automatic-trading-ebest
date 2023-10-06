import json
import requests
import asyncio
import websockets

class OverseesFuturesCls:
    # 해외선물마스터조회
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

    # 해외선물차트 분봉 조회
    def check_overseas_futures_charts(self, ACCESS_TOKEN):
        # 요청 url
        PATH = "overseas-futureoption/chart"
        URL = f"{self.BASE_URL}/{PATH}"

        # 요청 header
        header = {
            "content-type":"application/json; charset=utf-8",
            "authorization": f"Bearer {ACCESS_TOKEN}",
            "tr_cd":"o3103",
            "tr_cont":"N",
            "tr_cont_key":"",
        }

        # body
        body = {
              "o3103InBlock": {
                "shcode": "CUSV23",
                "ncnt": 1,
                "readcnt": 20,
                "cts_date": "",
                "cts_time": ""
              }
            }

        # 요청 보내기
        request = requests.post(URL, headers=header, data=json.dumps(body))
        result = request.json()
        print(result)
        return result

    # 해외선물차트 일주월 조회
    def overseas_futures_charts_weekly(self, ACCESS_TOKEN):
        # 요청 url
        PATH = "overseas-futureoption/chart"
        URL = f"{self.BASE_URL}/{PATH}"

        # 요청 header
        header = {
            "content-type": "application/json; charset=utf-8",
            "authorization": f"Bearer {ACCESS_TOKEN}",
            "tr_cd": "o3108",
            "tr_cont": "N",
            "tr_cont_key": "",
        }

        # body
        body = {
          "o3108InBlock": {
            "shcode": "CUSV23",
            "gubun": "0",
            "qrycnt": 20,
            "sdate": "20230502",
            "edate": "20230601",
            "cts_date": ""
          }
        }

        # 요청 보내기
        request = requests.post(URL, headers=header, data=json.dumps(body))
        result = request.json()
        print(result)
        return result