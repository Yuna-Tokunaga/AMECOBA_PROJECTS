#関数の中の変数について(スコープ変数)

grobal = 'world'

def say_rocal():
    msg = 'Japan'
    print(msg)

say_rocal()
print(grobal)

