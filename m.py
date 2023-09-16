while True:
    x = float(input("Enter a number: "))
    y = float(input("Enter a number: "))

    lowest = min(x , y)
    print( "The lowest number is:", lowest)
    
    choice = input("do you want to continue?: Y or N: ")
    if choice.lower() !="y":
        print("exit")
        break
    else:
        continue
    