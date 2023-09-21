import os
import configparser

def check_ini_file_exists(path):
    file_list = os.listdir(path)
    if any(file.endswith(".ini") for file in file_list):
        return 0
    else:
        return -1

path = "./"
result = check_ini_file_exists(path)

if result == 0:
    print(".ini 파일이 존재합니다.")
else:
    config = configparser.ConfigParser()

    # section => 'API_CONFIG'
    config['API_CONFIG'] = {
        'id': '',
        'pass': '',
        'certpass': '',
        'appkey': '',
        'secretkey ': '',
    }

    with open('./api_config.ini', 'w') as f:
        config.write(f)