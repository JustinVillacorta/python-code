while True:
    print("menu")
    print("A. Winter melon = 70.00 ")
    print("B. chocollate = 50.00 ")
    print("C. Strawberry 60.00")
    print("\nadd ons:")
    print("none = 0.00")
    print("A. pear = 5.00")
    print("B. nata = 10.00")

    menu = input("enter your choice ")
    add = input("enter your add ons ")

    if menu == "A" and add == "A":
        wintermelon_and_none = 70+0
        print("Total: " , float(wintermelon_and_none))
        payment1 = int(input("payment"))

        change1 = payment1 - wintermelon_and_none
        print("change: " , change1)

    elif menu == "A" and add == "B":
        wintermelon_and_pearl = 70+5
        print("Total: " , float(wintermelon_and_pearl))
        payment2 = int(input("payment"))
        change2 = payment2 - wintermelon_and_pearl
        print("change: " , change2)

    elif menu == "A" and add == "c":
        wintermelon_and_nata = 70+10
        print("Total: " , float(wintermelon_and_nata))
        payment3 = int(input("payment"))
        change3 = payment3 - wintermelon_and_nata
        print("change: " , change3)

    elif menu == "B" and add == "A":
        Chocolate_and_none = 50+0
        print("Total: " , float(Chocolate_and_none))
        payment4 = int(input("payment"))
        change4 = payment4 - Chocolate_and_none
        print("change: " , change4)

    elif menu == "B" and add == "B":
        chocolate_and_pearl = 50+5
        print("Total: " , float(chocolate_and_pearl))
        payment5 = int(input("payment"))
        change5 = payment5 - chocolate_and_pearl
        print("change: " , change5)

    elif menu == "B" and add == "C":
        chocolate_and_nata = 50+10
        print("Total: " , float(chocolate_and_nata))
        payment6 = int(input("payment"))
        change6 = payment6 -chocolate_and_nata
        print("change: " , change6)

    elif menu == "C" and add == "A":
        strawbery_and_none = 60+0
        print("Total: " , float(strawbery_and_none))
        payment7 = int(input("payment"))
        change7 = payment7 - strawbery_and_none
        print("change: " , change7)

    elif menu == "C" and add == "B":
        strawbery_and_pearl = 60+5
        print("Total: " , float(strawbery_and_pearl))
        payment8 = int(input("payment"))
        change8 = payment8 - strawbery_and_pearl
        print("change: " , change8)

    elif menu == "C" and add == "C":
        strawbery_and_nata = 60+10
        print("Total: " , float(strawbery_and_nata))
        payment9 = int(input("payment"))
        change9 = payment9 - strawbery_and_nata
        print("change: " , change9)

    choice = input("do you want to continue?: Y or N: ")
    if choice.lower() !="y":
        print("exit")
        break
    else:
        continue
    
    
    








