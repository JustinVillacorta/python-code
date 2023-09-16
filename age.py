while True:
    age = int(input(" enter age: "))

    if age <=18:
        print("young")

    elif age <= 59 and age >= 19:
         print("middle age")

    elif age <=60:
        print("old")
    else:
        print("realy old")

    choice = input("do you want to continue?: Y or N: ")
    if choice.lower() !="y":
        print("exit")
        break
    else:
        continue
    

