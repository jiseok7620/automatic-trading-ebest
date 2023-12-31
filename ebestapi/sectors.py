import json
import requests
import asyncio
import websockets

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

    # 예상지수
    def expected_index(self, ACCESS_TOKEN):
        # 요청 url
        PATH = "indtp/market-data"
        URL = f"{self.BASE_URL}/{PATH}"

        # 요청 header
        header = {
            "content-type": "application/json; charset=utf-8",
            "authorization": f"Bearer {ACCESS_TOKEN}",
            "tr_cd": "t1485",
            "tr_cont": "N",
            "tr_cont_key": "",
        }

        # body
        body = {
              "t1485InBlock" : {
                "upcode" : "001", # 업종코드 (코스피@001 코스닥@301 KRX100@501 KP200@101 SRI@515 코스닥프리미어@404 KRX 보험@516 KRX 운송@517)
                "gubun" : "1" # 조회구분 (1:장전 2:장후)
              }
            }

        # 요청 보내기
        request = requests.post(URL, headers=header, data=json.dumps(body))
        result = request.json()
        print(result)
        return result

    # 업종현재가
    def industry_current_price(self, ACCESS_TOKEN):
        # 요청 url
        PATH = "indtp/market-data"
        URL = f"{self.BASE_URL}/{PATH}"

        # 요청 header
        header = {
            "content-type": "application/json; charset=utf-8",
            "authorization": f"Bearer {ACCESS_TOKEN}",
            "tr_cd": "t1511",
            "tr_cont": "N",
            "tr_cont_key": "",
        }

        # body
        body = {
          "t1511InBlock" : {
            "upcode" : "001"
          }
        }

        # 요청 보내기
        request = requests.post(URL, headers=header, data=json.dumps(body))
        result = request.json()
        print(result)
        return result

    # [업종] 실시간 시세
    async def real_time_industry_price(self, ACCESS_TOKEN):
        # 웹 소켓에 접속을 합니다.
        async with websockets.connect(self.BASE_URL_REAL) as websocket:
            data = {
                 "header": {
                      "token": f"{ACCESS_TOKEN}", # 접근 토큰
                      "tr_type": "3" # 1: 계좌등록, 2: 계좌해제, 3: 실시간 시세 등록, 4: 실시간 시세 해제
                 },
                 "body": {
                      "tr_cd": "BM_", # 이베스트증권 거래코드(TR코드)
                      "tr_key": "001" # 단축코드 6자리 or 8자리
                 }
            }
            json_str = json.dumps(data)

            # 웹 소켓 서버로 데이터를 전송합니다.
            await websocket.send(json_str)

            while True:
                # 웹 소켓 서버로 부터 메시지가 오면 콘솔에 출력합니다.
                data = await websocket.recv()
                print(data)