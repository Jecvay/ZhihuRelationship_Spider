__author__ = 'Jecvay'

class Zhihu_Person:
    # 属性: 姓名, 关注的人列表, 粉丝列表
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.like = []
        self.beliked = []       # This var name(beliked) is suggested by FredChen

    # 添加关注的人
    def appendLike(self, id):
        if id not in self.like:
            self.like.append(id)

    # 添加粉丝
    def appedBeliked(self, id):
        if id not in self.beliked:
            self.beliked.append(id)

    # 显示关注的人
    def printLike(self):
        for id in self.like:
            print(id)

    # 显示粉丝
    def printBelike(self):
        for id in self.beliked:
            print(id)

