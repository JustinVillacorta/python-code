import random
while True:
    user = input("enter your pick (rock, paper, scissors): ")

    possible_actions = ["rock", "paper", "scissors"]
    computer = random.choice(possible_actions)
    print(f"\nYou chose {user}, computer chose {computer}.\n")

    if user == computer:
        print(f"Both player selected {user}. it's a tie" )

    elif user =="rock":
        if computer =="scissors":
            print("rock smahes scissors! you win")
    elif user =="rock":
        if computer =="paper":
            print("paper cover rock! computer win")
    elif user =="paper":
        if computer =="rock":
            print("paper cover rock! you win")

    elif user =="scissors":
        if computer =="rock":
            print("rock smahes scissors! computer win")

    elif user =="paper":
        if computer =="rock":
            print("paper smahes rock! you win")

    elif user =="rock":
        if computer =="paper":
            print("paper smahes rock! computer win win")

    elif user =="scissors":
        if computer =="paper":
            print("scissors smahes paper! you win")

    elif user =="paper":
        if computer =="scissors":
            print("scissors smahes paper! computer win")
    play = input("play agaian? Y/N: ")
    if play.lower() != "y":
        break
    


