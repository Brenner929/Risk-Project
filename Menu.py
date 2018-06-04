print("This is a Risk Scoring Tool\n")


def menu():
    print("Would you like to enter system information?")
    print("Y/N")
    choice = input()
    if choice == ("y" or "Y"):
        questions()
    elif choice == ("n" or "N"):
        quit()

menu()


