import json
import time
import requests


class YDMHttp:
    apiurl = 'http://api.yundama.com/api.php'
    username = ''
    password = ''
    appid = '4055'
    appkey = ''

    def __init__(self, name, passwd, app_id, app_key):
        self.username = name
        self.password = passwd
        self.appid = str(app_id)
        self.appkey = app_key

    def request(self, fields, files=[]):
        response = self.post_url(self.apiurl, fields, files)
        response = json.loads(response)
        return response

    def balance(self):
        data = {
            'method': 'balance',
            'username': self.username,
            'password': self.password,
            'appid': self.appid,
            'appkey': self.appkey
        }

        response = self.requests(data)
        if response:
            if response['ret'] and response['ret'] < 0:
                return response['ret']
            else:
                return response['balance']
        else:
            return -9001

    def login(self):
        data = {
            'method': 'login',
            'username': self.username,
            'password': self.password,
            'appid': self.appid,
            'appkey': self.appkey
        }
        response = self.request(data)
        if response:
            if response['ret'] and response['ret'] < 0:
                return response['ret']
            return response['uid']
        else:
            return -9001

    def upload(self, filename, codetype, timeout):
        data = {
            'method': 'upload',
            'username': self.username,
            'password': self.password,
            'appid': self.appid,
            'appkey': self.appkey,
            'codetype': str(codetype),
            'timeout': str(timeout)
        }

        file = {'file': filename}
        response = self.request(data, file)
        if response:
            if response['ret'] and response['ret'] < 0:
                return response['ret']
            else:
                return response['cid']
        else:
            return -9001

    def result(self, cid):
        data = {
            'method': 'result',
            'username': self.username,
            'password': self.password,
            'appid': self.appid,
            'appkey': self.appkey,
            'cid': str(cid)
        }
        response = self.request(data)
        return response and response['text'] or ''

    def decode(self, file_name, code_type, time_out):
        cid = self.upload(file_name, code_type, time_out)
        if cid > 0:
            for i in range(0, time_out):
                result = self.result(cid)
                if result != '':
                    return cid, result
                else:
                    time.sleep(1)
            return -3003, ''
        else:
            return cid, ''

    def post_url(self, url, fields, files=[]):
        for key in files:
            files[key] = open(files[key], 'rb')
        res = requests.post(url, files=files, data=fields)
        return res.text

    def code_verificate(name,
                        passwd,
                        file_name,
                        app_id=4055,
                        code_type=1005,
                        time_out=60):
        app_key = ''
        yundama_obj = YDMHttp(name, passwd, app_id, app_key)
        cur_uid = yundama_obj.login()
        print('uid: %s' % cur_uid)
        rest = yundama_obj.balance()
        print('balance:%s' % rest)
        #
        cid, result = yundama_obj.decode(file_name, code_type, time_out)
        print('cid: %s,result: %s' % (cid, result))
        return result

    if __name__ == "__main__":
        username = ''
        password = ''
        rs = code_verificate(username, password, 'pincode,png')
