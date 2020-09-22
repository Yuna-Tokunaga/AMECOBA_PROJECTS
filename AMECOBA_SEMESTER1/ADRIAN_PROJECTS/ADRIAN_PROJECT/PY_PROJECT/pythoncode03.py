import datetime

age = int(input('please input you age in here: '))


while True:
    try:
        if age < 21:
            print("You are so Young!")
            break
        else:
            print("you are so old.")
            break
    finally:
        print(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=0))))
        print('STATUS_CODE_200')