# pyxelとはゲームエンジンのライブラリー
# 参考記事：https://cpp-learning.com/pyxel_mouse/
# 参考記事：https://github.com/kitao/pyxel
# 参考記事：http://bknotthreedays.hatenablog.com/entry/2018/12/20/093537
import pyxel
 
WINDOW_H = 120
WINDOW_W = 160
CAT_H = 16
CAT_W = 16
 
class App:
    def __init__(self):
        pyxel.init(WINDOW_W, WINDOW_H, caption="Hello Pyxel")
        pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.image(1).load(0, 0, "assets/cat_16x16.png")
 
        pyxel.mouse(True)
        # pyxel.mouse(False)
 
        pyxel.run(self.update, self.draw)
 
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
 
    def draw(self):
        pyxel.cls(0)
        # pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(60, 65, 0, 0, 0, 38, 16)
        pyxel.blt(75, 45, 1, 0, 0, CAT_W, CAT_H, 5)
 
App()