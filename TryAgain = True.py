TryAgain = True

while TryAgain:
    try:
        Value = int(input("Whole number: "))
    except ValueError:
        print("You must enter a whole number!")
        try:
            choice = input("Try again (y/n)? ") 
        except :
            print("Ok, see you next time!")
            TryAgain = False
        else:
            if choice == "n" or choice == "N":
                TryAgain = False
            else:
                TryAgain = True
    except KeyboardInterrupt:
        TryAgain = False
    else:
        print(Value)
        TryAgain = True