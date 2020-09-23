persons = {"person_num1" : "1",
        "person_num2" : "2",
        "person_num3" : "3",
        "person_num4" : "4"
}


for person in persons:
    print(person)


fruits = {"apple" : "200",
        "banana" : "100",
        "orange" : "300"}


del fruits["banana"]  #バリューの方を指定したらKEYERRORが起こるから気をつけること


for fruit in fruits:
    print(fruit)



BOOKS = {"python": "1200",
        "ruby": "3000",
        "javascript":"2500"}


for BOOK in BOOKS:
    print(BOOK)