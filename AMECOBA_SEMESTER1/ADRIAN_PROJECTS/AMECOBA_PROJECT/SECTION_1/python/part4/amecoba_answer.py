import random

MAX = 100
MAX_STAGE = 10
print('1~{}の数を{}回以内で当ててください'.format(MAX, MAX_STAGE))

stage = 1

answer = random.randint(1, MAX)

while stage <= MAX_STAGE:
  print(stage, '回目 いくつかな：', end='')
  n = int(input())
  if n < 1 or n > MAX:
    continue
  if n == answer:
    print('answer', stage, '回で当たりました。')
    break
  elif n > answer:
    print('もっと小さな数です。')
  else:
    print('もっと大きな数です。')

  stage += 1

else:
  print('残念。正解は', answer, 'でした。')