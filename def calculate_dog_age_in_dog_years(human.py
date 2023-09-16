human = int(input("Input a dog’s age in human years: "))

if human <= 2:
    dogs = 10.5

elif human > 2:
    dogs = 21+(human-2)*4
    print((f"The dog's age in dog's years is {dogs}"))
else:
    print("invalid")    