__author__ = 'Jecvay'

import Zhihu_urllib
import Zhihu_Login  # for
import Zhihu_Person
import re

from collections import deque

class Zhihu_Relation :
    def __init__(self, opener):
        self.opener = opener
        self.ZhiIdList = []
        self.ZhiPersonList = {}       # (id, obj)

    def fetchLike(self, id):
        op = self.opener.open('http://www.zhihu.com/people/' + id + '/followees')
        data = Zhihu_urllib.ungzip(op.read()).decode()
        nameList = []
        recp = re.compile('<a title="(.*)"\ndata-tip="p\$t\$(.*)"', re.M)
        nameList = recp.findall(data)
        return nameList

    def fetchBeLiked(self, id):
        op = self.opener.open('http://www.zhihu.com/people/' + id + '/followers')
        data = Zhihu_urllib.ungzip(op.read()).decode()
        nameList = []
        recp = re.compile('<a title="(.*)"\ndata-tip="p\$t\$(.*)"', re.M)
        nameList = recp.findall(data)
        return nameList

    def fetchName(self, id):
        op = self.opener.open('http://www.zhihu.com/people/' + id)
        data = Zhihu_urllib.ungzip(op.read()).decode()
        recp = re.compile('<title> (.*) - 知乎</title>')
        nameList = recp.findall(data)
        return nameList[0]

    def bfs(self, id):
        if id not in self.ZhiIdList:
            q = deque([id])
            name = self.fetchName(id)
            self.ZhiIdList.append(id)
            self.ZhiPersonList[id] = Zhihu_Person.Zhihu_Person(id, name)

        while q:
            id = q.popleft()
            print('BFS Connect to id:', id)

            nameList = self.fetchLike(id)
            for nname, nid in nameList:
                print('BFS dealing with: ' + id + ' like --> ' + '(' + nid + ', ' + nname + ')')
                if nid not in self.ZhiIdList:
                    self.ZhiPersonList[nid] = Zhihu_Person.Zhihu_Person(nid, nname)
                    self.ZhiIdList.append(nid)
                    q.append(nid)

            nameList = self.fetchBeLiked(id)
            for nname, nid in nameList:
                print('BFS dealing with: (' + nid + ', ' + nname + ')' + ' --> like ' + id)
                if nid not in self.ZhiIdList:
                    self.ZhiPersonList[nid] = Zhihu_Person.Zhihu_Person(nid, nname)
                    self.ZhiIdList.append(nid)
                    q.append(nid)

print("Tester: Zhihu_Relation")
opener = Zhihu_Login.loginZhiHu('ljwjiewei@gmail.com', 'bcdljw38')
relationSystem = Zhihu_Relation(opener)
relationSystem.bfs('ourdearamy')