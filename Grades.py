
while True:
    p1 = int(input("enter P1 grade: "))
    p2 = int(input("enter p2 grade: "))
    p3 = int(input("enter p3 grade: "))

    ave = (p1 + p2 + p3)/3

    if ave >=90:
        print("your Average is" , ave)
        print("Your grade is A")

    elif ave <= 90 and ave >= 80:
        print("your Average is" , ave)
        print("Your grade is B")


    elif ave <= 80 and ave >= 60:
        print("your Average is" , ave)
        print("Your grade is C")


    else:
        print("your Average is" , ave)
        print("Your grade is D")

    choice = input("do you want to continue?: Y or N: ")
    if choice.lower() !="y":
        print("exit")
        break
    else:
        continue
    