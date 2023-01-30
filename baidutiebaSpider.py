from urllib import request
from urllib import parse
import time
import random

class BaiduTiebaSpider:
    def __init__(self):
        self.ur1 = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=8452201&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

    def get_html(self, url):
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()

        return html

    def parse_html(self):
        """解析提取数据的函数"""

        pass

    def save_html(self, filename, html):
        with open(filename, 'w', encoding='utf8') as f:
            f.write(html)

    def run(self):
        name = input('请输入贴吧名：')
        start = int(input('请输入起始页：'))
        end = int(input('请输入终止页：'))
        params = parse.quote(name)
        # 1.拼接url地址
        for page in range(start, end + 1):
            pn = (page - 1) * 50  # 根据所选贴吧url规律计算得出
            url = self.ur1.format(params, pn)
            html = self.get_html(url)
            filename = '{}_第{}页.html'.format(name, page)
            self.save_html(filename, html)
            # 终端打印提示
            print('第%d页抓取成功' % page)
            # 控制数据抓取的频率
            time.sleep(random.randint(1, 3))


test = BaiduTiebaSpider()
test.run()




