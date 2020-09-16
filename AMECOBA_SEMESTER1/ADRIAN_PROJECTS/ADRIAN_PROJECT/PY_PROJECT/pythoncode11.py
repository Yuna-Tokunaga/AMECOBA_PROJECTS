# 例外処理について

# try：

# except Exception as ex:
#     print('エラーが発生しました')
    


# try:
#     data = 5 / 0
# except Exception:
#     print('Exception')
# except ArithmeticError:
#     print('ArithmeticError')
# except OverflowError:
#     print('OverflowError')


file = None

try:
    file = open('hello.txt','r',encoding='UTF-8')
    data = file.read()
    print(data)
finally:
    if file:
        file.close()