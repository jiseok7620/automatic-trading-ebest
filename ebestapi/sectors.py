import json
import requests

'''
@HEADER
>>> content-type : 이베스트증권 제공 API를 호출하기 위한 Request Body 데이터 포맷으로 "application/json; charset=utf-8 설정"
>>> authorization : OAuth 토큰이 필요한 API 경우 발급한 Access Token을 설정하기 위한 Request Heaeder Parameter
>>> tr_cd : 이베스트증권 거래코드
>>> tr_cont : 연속거래 여부 (Y : 연속, N : 불연속)
>>> tr_cont_key : 연속 거래 Key, 연속일 경우 그전에 내려온 연속키 값 올림
>>> mac_address : MAC 주소, 법인인 경우 필수 세팅
'''
class SectorsQuote:
    # 업종기간별추이
    def trand_by_industry_period(self, ACCESS_TOKEN):
        # 요청 url
        PATH = "indtp/market-data"
        URL = f"{self.BASE_URL}/{PATH}"

        # 요청 header
        header = {
            "content-type":"application/json; charset=utf-8",
            "authorization": f"Bearer {ACCESS_TOKEN}",
            "tr_cd":"t1514",
            "tr_cont":"N",
            "tr_cont_key":"",
        }

        # body
        body = {
                "t1514InBlock": {
                    "upcode": "001", # 업종코드
                    "gubun1": " ", # 구분1 (미사용항목 - 스페이스설정)
                    "gubun2": "1", # 구분2 (1:주, 2:월, 3:분)
                    "cts_date": " ", # CTS_일자 (처음조회시 스페이스, 연속조회시 이전조회한 cts_date값으로 설정)
                    "cnt": 1, # 조회건수
                    "rate_gbn": "1" # 비중구분 (1:거래량비중, 2:거래대금비중)
                }
            }

        # 요청 보내기
        request = requests.post(URL, headers=header, data=json.dumps(body))
        result = request.json()
        print(result)
        return result

    # 전체업종
    def all_industries(self, ACCESS_TOKEN):
        # 요청 url
        PATH = "indtp/market-data"
        URL = f"{self.BASE_URL}/{PATH}"

        # 요청 header
        header = {
            "content-type":"application/json; charset=utf-8",
            "authorization": f"Bearer {ACCESS_TOKEN}",
            "tr_cd":"t8424",
            "tr_cont":"N",
            "tr_cont_key":"",
        }

        # body
        body = {
                "t8424InBlock": {
                "gubun1": ""
              }
            }

        # 요청 보내기
        request = requests.post(URL, headers=header, data=json.dumps(body))
        result = request.json()
        print(result)
        return result