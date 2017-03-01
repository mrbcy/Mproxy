#-*- coding: utf-8 -*-

import requests

def func():
    headers = {
        "Host": "www.kuaidaili.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://onlinelibrary.wiley.com/journal/10.1002/(ISSN)1521-3773",
        "Cookie": "_gat=1; channelid=0; sid=1488211261856538; _ga=GA1.2.167063512.1488083088; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1488083088,1488174082,1488205850,1488211463; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1488211463",
        "Connection": "keep-alive",
        "Upgrade - Insecure - Requests": "1"
    }

    r = requests.get('http://www.kuaidaili.com/?yundun=2dd18b5fbdf705420548',headers=headers)
    print(r.text)


if __name__ == '__main__':
    func()