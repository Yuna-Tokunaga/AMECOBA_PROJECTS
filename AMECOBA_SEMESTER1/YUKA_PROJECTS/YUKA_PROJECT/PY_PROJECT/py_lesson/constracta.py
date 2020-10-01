# クラス

#class User: #クラスの最初の文字は大文字
   # pass

#tom = User()
#tom.name = "tom"
#tom.score = 20

#bob = User()
#bob.name = 'bob'
#bob.level = 5

class User:
    def __init__(self, name):
        # インスタンス変数
        self.name = name

yuka = User("mom")
bob = User("dad")

print(yuka.name)
print(bob.name)
