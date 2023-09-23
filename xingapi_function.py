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

class Login_Ebest:
    def Login(self):
        # id, password, 공인인증서패스워드 지정
        id = "ghkd7620"
        passwd = "js1016@#"
        cert_passwd = "js101600?!"

        # xingAPI와 COM으로 통신할 이벤트 클래스를 연결해주는작업을 하게됨
        # => Login_Ebest 클래스에서 정보를 요청하면 이베스트서버에서 응답한 정보를 XASessionEvents 클래스에서 받음
        self.instXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEvents)
        self.instXASession.ConnectServer("hts.ebestsec.co.kr", 20001)
        self.instXASession.Login(ebest_id, ebest_pass, ebest_certpass, 0, 0)

class XASessionEvents:
    logInState = 0
    def OnLogin(self, code, msg):
        print("onLogin method is called")
        print(str(code))
        print(str(msg))

        # 0000이 입력될 때만 로그인 성공
        if str(code) == '0000':
            XASessionEvents.logInState = 1
        else:
            XASessionEvents.logInState = 0

conn = Login_Ebest()
conn.Login()