# 月山蘭 から 皆様 : (6:16 午後)
# 整数を1から100まで順に数え上げながら、* 3 で割り切れるとき、 Fizz を出力* 5 で割り切れるとき、 Buzz を出力* 15 で割り切れるとき、 Fizz Buzz を出力* それ以外のとき、数値をそのまま出力するコードを書け。



for i in range(100):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print("???")