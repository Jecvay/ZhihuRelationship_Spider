__author__ = 'Jecvay'
import urllib.request
import urllib.parse
import Zhihu_urllib



header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.zhihu.com',
    'DNT': '1'
}


# 根据用户名密码, 返回一个已经登录了知乎网的 opener, 此 opener 有 Cookie
def loginZhiHu(id, password):
    postDict = {
        'email': id,
        'password': password,
        'rememberme': 'y'
    }
    header['referer'] = 'http://www.zhihu.com/#signin'
    header['X-Requested-With'] = 'XMLHttpRequest'

    opener = Zhihu_urllib.getOpener(header)

    url = 'http://www.zhihu.com/'

    ########################### GET
    op = opener.open(url)

    data = op.read()    # 读取回来可能是经过压缩的, 需要解压
    data = Zhihu_urllib.ungzip(data)  # 尝试解压
    Zhihu_urllib.saveFile(data)

    ########################### POST
    postDict['_xsrf'] = Zhihu_urllib.getXSRF(data.decode())
    postData = urllib.parse.urlencode(postDict)
    op = opener.open(url + 'login', data = postData.encode())
    data = Zhihu_urllib.ungzip(op.read())
    return opener

# print("Tester: Zhihu_login")
# loginZhiHu('ljwjiewei@gmail.com', 'bcdljw38')