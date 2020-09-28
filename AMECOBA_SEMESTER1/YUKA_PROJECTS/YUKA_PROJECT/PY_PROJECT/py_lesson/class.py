#クラス 複雑なデータコードを作るための仕組

#user_name = 'yuka'
#user_score = 100


# userに関するデータをまとめるためにクラスを作る

class User: #下の物をクラスのインスタンスと言う。
    pass #中身の無いクラス

cat = User()
cat.name = 'candy'
cat.old = 10

dog = User()
dog.name = 'lucky'
dog.old = 6

print(cat.name)
print(dog.name)