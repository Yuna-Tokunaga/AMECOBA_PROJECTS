#端末で初めてのHELLOWORLDを出力してみよう

print("hello world")

print(10-1)

#文字列や数字を合わせて表示する

print("NUMBER", 10 + 2)

print("WELCOME" + "to" + "AMECOBA")

#モジュール（部品）を使って簡単なおみくじプログラムを作ってみよう

import random #シャフルするので、Randomという部品を使います。

kujibiki = ["VERY LUCKY", "LUCKY", "GOOD", "NOT BAD", "BAD", "VERY BARD"]

#変数　= [要素0, 要素1, 要素2, 要素3, 要素4, 要素5]

print(random.choice(kujibiki))

#出力(モジュール.選ぶ(変数))


#BMI直計算プログラムの身長と体重の総合を測ってみよう

HEIGHT = float(input("身長何センチですか？"))

#身長　=　浮動小数点(入力（"身長何センチですか？"）)

WEIGHT = float(input("体重何キロですか？"))

#体重 = 浮動小数点（入力（"体重何キロですか？"））

BMI = WEIGHT / (HEIGHT * HEIGHT)

#BMI = 体重 / (身長　✖️　身長)

print("あなたのBMI値:", BMI, "ですね！")

#出力（"あなたのBMI値", BMI(変数), "ですね！"）



#様々なデータの種類を理解しよう
#変数に入れることができるデータには、「数値」、「文字」などいろいろな種類がある　＝　データ型

number = 100

float_number = 13.2

string_word = "hello"

b = True #反対はFalse

print(type(number)) #個数や順番に使う

print(type(float_number)) #一般的な計算に使う

print(type(string_word)) #文字数を扱う時に使う

print(type(b)) #true か　false かの二択の時に使う

#文字列の操作を覚えよう

write = "hello" + "my name is amecoba"

print(write)

print(len(write)) #文字数を調べる lenメソッド


print(write[0]) #出力(変数[要素番号])

print(write[6:12]) #出力(変数[開始要素番号：最後の要素番号から一つ前])

print(write[-3:]) ##出力(変数[逆の要素番号])


print("hello \n world.") #文字列を改行

print("hello wo\trld.") #タブ文字

#データ型を変換する

a = "100"

print(a + 23) # TypeError なぜかというと 100という数字ではなく、文字列として扱われているから

print(int(a) + 23) #123

#変換できない時はエラーになる


b = "hello"


print(int(b) + 23) #Type Error

#isdigitメソッドを用いて数値に変換できるのか


a = "100"

b = "hello"

print(a.isdigit())
print(b.isdigit())


#データをまとめるためのリストを使ってみよう

fruits = ["apple", "banana", "cherry", "blueberry"]

print(fruits[2])


#===========================================================================


#if文を使ってみよう

#if 条件式：
    #条件式が正しい時にする処理

tennsu = 100

if tennsu >= 80: #もしも
    #>=とは　比較演算子
    print("Good job!")

elif tennsu >= 60: #そうでないけれど、もしも
    print("good")

else: #そうでないとき
    print("Don't worry about tennsu")


#for文を使ってみよう

#for カウント変数 in range(回数):
    #繰り返す処理

for i in range(10):
    print(i)

#for文を使ってリストを取り出しみる

#for　要素をいれる変数 in リスト：
    #繰り返す処理


score = [64, 100, 78, 80, 72]

for i in score:
    print(i)



#for文によるネスト化（入れ子）

#for カウント変数 in range(回数):
    #for カウント変数 in range(回数):
    #  繰り返す処理


for i in range(10):
    for j in range(10):
        print(j * i)


#def関数を使って簡単に一つ

#def　関数名():
    # 関数で行う処理

def hello():
    print("hello")


hello()

# return を使う

# def 関数名（引数1, 引数2）:
    # 関数で行う処理
    # return 戻り値



def postTaxPrice():
    ans = 100 * 1.08
    return ans
    # print("hello") #呼び出されることはない, returnがあるので

print(postTaxPrice())