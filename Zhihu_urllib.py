__author__ = 'Jecvay'

import http.cookiejar
import urllib.request
import gzip
import http.cookiejar
import re

# head: 自定义发送的header
# 返回一个自定义opener
def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

def saveFile(data):
    save_path = 'D:\\temp.txt'
    f = open(save_path, 'wb')
    f.write(data)
    f.close()

# data: 传入第一遍GET回来的zhihu登录页面, 用于提取_xsrf码, 以便下一步post
def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]

def ungzip(data):
    try:        # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data