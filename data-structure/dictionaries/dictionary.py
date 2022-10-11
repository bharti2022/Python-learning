empty_dict = {}  # Empty dictionary
print(empty_dict)

phone_book = {"Batman": 468426,
              "Ghostbusters": 44678,
              "Cersei": 237734,
              "Ghostbusters": 44578}
print(phone_book)
print(phone_book.get("Batman"))

#using dict() constructor
phone_book = dict(number1=1234, number2=122345, number3=123456)
print(phone_book)
print(phone_book.get("number1"))

#update a value
phone_book["number1"]=1234567
#delete a value
del phone_book["number3"]

# check key xisting or not
print("number1" in phone_book)
houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)


