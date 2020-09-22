import requests
import datetime

requests = requests.get("https://github.com/adrian-zulnedi")

try:
    with open('github.html', 'w') as file:
        print(datetime.datetime.now())
        file.write(requests.text)
        print('作成に成功しました')

except:
   print('作成に失敗しました')