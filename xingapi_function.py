import configparser
import win32com.client
import pythoncom

# configparser Object Create
config = configparser.ConfigParser()

# .ini file load
config.read('./API_CONFIG.ini')

# 섹션과 키로 값 읽기
ebest_id = config.get('API_CONFIG', 'id') # 아이디
ebest_pass = config.get('API_CONFIG', 'pass') # 비밀번호
ebest_certpass = config.get('API_CONFIG', 'certpass') # 공인인증서 비밀번호
ebest_appkey = config.get('API_CONFIG', 'appkey')
ebest_secretkey = config.get('API_CONFIG', 'secretkey')

# XASession 객체 생성
instXASession = win32com.client.Dispatch("XA_Session.XASession")

# 이미 연결되어 있다면 연결 끊기
if instXASession.IsConnected() == 1:
    instXASession.DisconnectServer()

# 서버 접속 정보 설정
'''
실서버 : hts.ebestsec.co.kr
모의서버 : demo.ebestsec.co.kr 
'''
instXASession.ConnectServer("hts.ebestsec.co.kr", 20001)

# 사용자 정보 입력 후 로그인 시도
instXASession.Login(ebest_id, ebest_pass, ebest_certpass, 0, False)

while True:
    # 로그인 요청에 대한 응답을 기다림
    pythoncom.PumpWaitingMessages()

    # 연결 상태 확인: 1 - 연결됨, 0 - 미연결
    if instXASession.IsConnected() == 1:
        print("로그인 성공")
        break
    elif instXASession.IsConnected() == 0:
        print("로그인 실패")
        break

# 계좌 개수 가져오기
account_count = instXASession.GetAccountListCount()
print(">>> 계좌 개수 :", account_count)

# 계좌 리스트 가져오기
for i in range(account_count):
    account = instXASession.GetAccountList(i)
    print(">>> 계좌 번호 :", account)