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

    # 해외선물 일별체결 조회
    def overseas_futures_daily_trading_inquiry(self, ACCESS_TOKEN):
        # 요청 url
        PATH = "overseas-futureoption/market-data"
        URL = f"{self.BASE_URL}/{PATH}"

        # 요청 header
        header = {
            "content-type":"application/json; charset=utf-8",
            "authorization": f"Bearer {ACCESS_TOKEN}",
            "tr_cd":"o3104",
            "tr_cont":"N",
            "tr_cont_key":"",
        }

        # body
        body = {
          "o3104InBlock": {
            "gubun": "0",
            "shcode": "CUSV23",
            "date": "20230908"
          }
        }

        # 요청 보내기
        request = requests.post(URL, headers=header, data=json.dumps(body))
        result = request.json()
        print(result)
        return result

    # 해외선물 현재가(종목정보) 조회
    def overseas_futures_stock_information(self, ACCESS_TOKEN):
        # 요청 url
        PATH = "overseas-futureoption/market-data"
        URL = f"{self.BASE_URL}/{PATH}"

        # 요청 header
        header = {
            "content-type":"application/json; charset=utf-8",
            "authorization": f"Bearer {ACCESS_TOKEN}",
            "tr_cd":"o3105",
            "tr_cont":"N",
            "tr_cont_key":"",
        }

        # body
        body = {
           "o3105InBlock" :{
              "symbol" : "CUSV23"
           }
        }

        # 요청 보내기
        request = requests.post(URL, headers=header, data=json.dumps(body))
        result = request.json()
        print(result)
        return result

    # 해외선물 현재가호가 조회
    def current_price_overseas_futures(self, ACCESS_TOKEN):
        # 요청 url
        PATH = "overseas-futureoption/market-data"
        URL = f"{self.BASE_URL}/{PATH}"

        # 요청 header
        header = {
            "content-type": "application/json; charset=utf-8",
            "authorization": f"Bearer {ACCESS_TOKEN}",
            "tr_cd": "o3106",
            "tr_cont": "N",
            "tr_cont_key": "",
        }

        # body
        body = {
            "o3106InBlock": {
                "symbol": "CUSV23"
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