#参考記事：　https://qiita.com/git-Ktu/items/8140ae6b2e3d2bfe4ed9

from PIL import Image 

#画像の名前を入力する
original = input("画像の名前を入れる>>")
#元となる画像
image = Image.open(original)
#画像を8ビット/256階調グレースケールにし、オリジナルの名前＋-grayscale.jpgで保存する
image.convert("L").save(original+"-grayscale.jpg")