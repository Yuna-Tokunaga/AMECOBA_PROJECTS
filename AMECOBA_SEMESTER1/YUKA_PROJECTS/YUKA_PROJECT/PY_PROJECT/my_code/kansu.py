# 関数・・・複数の処理をまとめて名前をつける事ができる

#def say_yuka():
#    print('Perfect')

#say_yuka()

def say_family(name,age = 20):
    print('yuka {0}({1})'.format(name, age))


say_family('dad',52)
say_family('mom',)
say_family(age = 18, name = 'bro')