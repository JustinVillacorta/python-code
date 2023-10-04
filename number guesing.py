import random
while True:
    user = int(input("Enter a number: "))

    for possible_actions in range (1, 101): 
        computer = random.choice(possible_actions)
        print(possible_actions)

    
    if user == computer:
        print(f"user guess the correct number" )
        break
    
    else:
        print("try again")
   
    play = input("do want to continue? Y/N: ")

    if play.lower() != "y":
        break


