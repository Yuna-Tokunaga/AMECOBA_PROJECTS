# 1.ファイル名は「test_対象のモジュール名.py」とする
import unittest
import calc
 
# 2.テストクラス名は「Testテスト対象のクラス名」とする
# 3.テストクラスはunittest.TestCaseを継承する
class TestCalc(unittest.TestCase):
 
  # 4.テストメソッド名は「test_テスト対象のメソッド名」とする(以下同)
  def test_add_num(self):
    self.assertEqual(10, calc.add_num(6, 4)) 
 
  def test_sub_num(self):
    self.assertEqual(2, calc.sub_num(6, 4))

  def test_mul_num(self):
    self.assertEqual(24, calc.mul_num(6, 4))

  def test_div_num(self):
    self.assertEqual(10, calc.div_num(6, 4))