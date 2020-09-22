#-----------------------------------------------------------------------------------------------#
# 参考記事: https://www.youtube.com/watch?v=iGGrklV_AC4&ab_channel=%E3%80%90IT%E3%83%BB%E3%83%9
# 7%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0Lab%E3%80%91%E4%BC%8A%E6%B2%A2%E5%89%9B
#-----------------------------------------------------------------------------------------------#


import pandas as pd #エクセルのブックを操作するライブラリの読み込み

item_list = [] #エクセルのブックを操作するライブラリの読み込み

item_no = input("商品番号を入力してください　終了は-1:") #エクセルに出力するデータを格納するリスト

while(int(item_no) != -1): #商品番号に-1 が入力されるまで15行目から21行目まで繰り返す

    item_name = input("商品名を入力してください:")

    item_price = input("価格を入力してください:")

    item_list.append([item_no, item_name, item_price]) #入力したデータをリスト形式で追加
    
    item_no = input("商品番号を入力して下さい 終了は-1:")

df = pd.DataFrame(item_list ,columns=['商品番号', '商品名', '価格']) #列名

with pd.ExcelWriter("商品リスト.xlsx") as writer:
    df.to_excel(writer, index=False) #エクセルファィルに書き出し

print("プログラム終了")