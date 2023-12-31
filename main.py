import configparser
import requests
from ebestapi import sectors
from ebestapi import overseas_futures
import asyncio

# 접근 토큰 발급 받기
def AccessToken(APP_KEY, APP_SECRET):
    header = {"content-type": "application/x-www-form-urlencoded"}
    param = {"grant_type": "client_credentials", "appkey": APP_KEY, "appsecretkey": APP_SECRET, "scope": "oob"}
    PATH = "oauth2/token"
    BASE_URL = "https://openapi.ebestsec.co.kr:8080"
    URL = f"{BASE_URL}/{PATH}"

    request = requests.post(URL, verify=False, headers=header, params=param)
    ACCESS_TOKEN = request.json()["access_token"]
    return ACCESS_TOKEN

class Main:
    def __init__(self):
        config = configparser.ConfigParser() # configparser Object Create
        config.read('./API_CONFIG.ini') # .ini file load

        # 전역 변수 설정
        self.EBEST_APPKEY = config.get('API_CONFIG', 'appkey')
        self.EBEST_SECRETKEY = config.get('API_CONFIG', 'secretkey')
        self.BASE_URL = "https://openapi.ebestsec.co.kr:8080"
        self.BASE_URL_REAL = "wss://openapi.ebestsec.co.kr:9443/websocket"
        self.ACCESS_TOKEN = AccessToken(self.EBEST_APPKEY, self.EBEST_SECRETKEY)

    def main(self):
        # 단일 조회
        #sector_quote = sectors.SectorsQuote.trand_by_industry_period(self, self.ACCESS_TOKEN)
        #all_industry = sectors.SectorsQuote.all_industries(self, self.ACCESS_TOKEN)
        #expect_index = sectors.SectorsQuote.expected_index(self, self.ACCESS_TOKEN)
        #industry_current_price = sectors.SectorsQuote.industry_current_price(self, self.ACCESS_TOKEN)

        # 단일 조회 (해외선물)
        #overseas_futures.OverseesFuturesCls.oversees_futures_master_inquiry(self, self.ACCESS_TOKEN)
        #overseas_futures.OverseesFuturesCls.check_overseas_futures_charts(self, self.ACCESS_TOKEN)
        #overseas_futures.OverseesFuturesCls.overseas_futures_charts_weekly(self,self.ACCESS_TOKEN)
        #overseas_futures.OverseesFuturesCls.overseas_futures_daily_trading_inquiry(self,self.ACCESS_TOKEN)
        overseas_futures.OverseesFuturesCls.overseas_futures_stock_information(self,self.ACCESS_TOKEN)
        overseas_futures.OverseesFuturesCls.current_price_overseas_futures(self,self.ACCESS_TOKEN)

        # 실시간 조회
        #asyncio.get_event_loop().run_until_complete(sectors.SectorsQuote.real_time_industry_price(self, self.ACCESS_TOKEN))

if __name__ == "__main__":
    ins_main = Main()
    ins_main.main()