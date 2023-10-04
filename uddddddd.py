while True: 

    convice = input("Will she stay in UPang? (Yes or No): ")
    if convice.lower() == 'yes':
        print("She stays in UPang")
    elif convice.lower() == 'no':
        decision = input("Are you sure?: ")
        if decision.lower() != 'no':
            print("Ok, where will she study?")
            school = input("School: ")
            if school.lower() == 'udd':
                print("BRUUUHH, TRASH SCHOOL")
            else:
                print("Nice, not a trash school")

    again = input("Try again?: ")
    if again.lower() != 'yes':
        print(f"I guess she'll go to {school}")
        break