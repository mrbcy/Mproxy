#-*- coding: utf-8 -*-

import requests

def func():
    headers = {
        "Host": "www.xicidaili.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        # "Referer": "http://onlinelibrary.wiley.com/journal/10.1002/(ISSN)1521-3773",
        # "Cookie": "UM_distinctid=15acc3845b41b18-0d8ce788886474-6776a51-1fa400-15acc3845b8139c; _free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTc5M2NkNjdiMTBiNWFlOWIyOTZiOGIzODQ2OGZjZTdmBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWNabVdjYlNvNE82MDlRT3FlM3Y3YU5UWldDWHdoMDNOcWRjbXUvNEhMa1k9BjsARg%3D%3D--ab7e6c0c5dee8cd31f33c804e3b5988289722c34; CNZZDATA1256960793=132924651-1488081082-http%253A%252F%252Fwww.baidu.com%252F%7C1489481220",
        "Connection": "keep-alive",
        "Upgrade - Insecure - Requests": "1"
    }
    session = requests.Session()
    r = session.get('http://www.xicidaili.com/nn/',headers=headers)
    r = session.get('http://www.xicidaili.com/nn/',headers=headers)
    print(r.text)


if __name__ == '__main__':
    func()