import datetime
import locale

locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')

dt = datetime.datetime.now()


print(dt)
print(dt.strftime('%c'))
print(dt.strftime('%x'))
print(dt.strftime('%X'))
print(dt.strftime('%Y年 %m月 %d日 (%a) %I時 %M分'))
