#-*- coding: utf-8 -*-
import re
import requests


def valid_proxy():
    headers = {
        "Host": "www.baidu.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Cookie": "CXID=AFB58656EB6137C12D0E4FF12BC6DFFE; SUV=1484628390086037; m=FAB6EC92D3062F7D84CC06636E62F609; ABTEST=0|1486986265|v17; ad=oe45yZllll2Y$gmTlllllVAIWEtlllllJa0oJyllll9lllll9Zlll5@@@@@@@@@@; SUID=B96B30B65412940A00000000586E6482; ld=okllllllll2Y7@v2lllllVA8dw1lllllH0xrAlllll9lllllpZlll5@@@@@@@@@@; YYID=FAB6EC92D3062F7D84CC06636E62F609; SNUID=441BB6B17B7E35AEB86CFBF37CECC35E; usid=Ibgtjb1FmwpmVEd9; IPLOC=CN1101; browerV=8; osV=1",
        "Connection": "keep-alive",
        "Upgrade - Insecure - Requests": "1"
    }
    res = requests.get('http://www.sogou.com/',proxies = {'http':'120.77.156.50:80'})
    regex = """050897"""
    pattern = re.compile(regex)
    if re.search(pattern=pattern,string=res.text) is not None:
        print "proxy is available"
    else:
        print "proxy is unavailable"

if __name__ == '__main__':
    valid_proxy()