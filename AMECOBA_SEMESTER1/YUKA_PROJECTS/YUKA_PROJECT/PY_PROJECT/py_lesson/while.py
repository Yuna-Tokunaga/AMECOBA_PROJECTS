#ループ処理　いわゆる繰り返し処理
i = 0
while i < 10:
    if i == 5:
        break #breakの後のelseの処理は行われない。
    print(i)
    i += 1
else:
    print('おしまい')