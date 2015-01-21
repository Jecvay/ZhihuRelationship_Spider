__author__ = 'Jecvay'
import Zhihu_Login
import Zhihu_Person



# 1. 从我出发扫到很多人, 加入我的列表
# 2. 加入广搜队列, 变成从队首元素出发, 执行1

def bfs:
    opener = Zhihu_Login.loginZhiHu('ljwjiewei@gmail.com', 'bcdljw38')
    d = opener.open('http://www.zhihu.com/people/jecvay/followees')