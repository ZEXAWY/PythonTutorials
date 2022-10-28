while True:
    select_option = input("Select 'a', 'b', 'c', 'd','e', or 'q' to quite. ")
    if select_option == 'a':
        print(f"You entered: ({select_option})")
    elif select_option == 'b':
        print(f"You entered: ({select_option})")
    elif select_option == 'c':
        print(f"You entered: ({select_option})")
    elif select_option == 'd':
        print(f"You entered: ({select_option})")
    elif select_option == 'e':
        print(f"You entered: ({select_option})")
    elif select_option == 'q':
        confirmation = input("are you sure you want to quite? [y/n].")
        if confirmation == 'y':
            print("see you later.")
            break
        elif confirmation == 'n':
            pass
        else:
            print(f"You entered {confirmation} and its not acceptable.")
    else:
        print("you entered invalid option.")