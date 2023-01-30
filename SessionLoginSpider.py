import requests

class DMPSpider:
    def __init__(self):
        self.url = 'http://192.168.1.1/venus/deviceControlInstruction/get?id=11'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8'}

    def html_login(self):
        login_url='http://172.16.5.87/venus/api/coreresource/auth/login/v1'
        from_data={'userName':'admin','password':'123456'}
        session=requests.Session()
        data=session.post(login_url,json=from_data,headers=self.header).text
        return session

    def getDeviceInfo(self,session,url,header):
        # 获得相应对象
        res = session.get(url=url, headers=header).text
        #获取网页源代码（默认是字节串，需要转为字符串）
        return res

    def run(self):
        print('='*30)
        url=self.url
        header=self.header
        session=self.html_login()
        context=self.getDeviceInfo(session,url,header)
        print(context)
        print('='*30)

a=DMPSpider()
a.run()


