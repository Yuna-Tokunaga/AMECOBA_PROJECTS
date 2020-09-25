# for ループ処理

# for 変数 in データの集合(rangeと言う命令で作れる):
#   処理

#for i in range(0,10):↓0からの場合0なくても同じ処理ができる
for i in range(10):
    if i == 5:
        # break
        continue # 変数がifの支持した通りの時にスキップする
    print(i)
else:
    print('end')