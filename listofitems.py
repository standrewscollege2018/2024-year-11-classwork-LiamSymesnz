items = []
run_program = True
while run_program:
    get_choice = True
    while get_choice:
        try:
            choice = int(input(print("Menu\n========================\n1. See all items in list\n2. Add items to list\n3. Delete item from list\n")))
            if choice >= 4 or choice <= 0:
                print("You need to enter a valid number")
            else:
                get_choice = False
        except ValueError:
            print("Enter a valid number\n")

    if choice == 1:
        if len(items) == 0:
            print("You cant print anything, theres nothing in your list\n")
        else:
            for i in range (len(items)):
                print(f"{i+1} {items[i]}")

    elif choice == 2:
        add = True
        while add:
            try:
                add_item = input("What item do you want to add? Say stop to stop and go back to menu\n")
                if add_item.lower().strip() == "stop":
                    add = False
                elif add_item.strip() == "":
                    print("You need an input\n")
                else:
                    items.append(add_item)

            except ValueError:
                    print("Enter a valid input")

    elif choice == 3:
        if len(items) == 0:
            print("You cant delete anything, theres nothing in the list")
        else:
            try:
                for i in range (len(items)):
                    print(f"{i+1} {items[i]}")
                delete = int(input("What item do you want to delete? (enter the number relevant)\n"))
                if delete >= (len(items+1)) or delete <= (len(items-1)):
                    print("You need to enter a number that refers to an item")
                else:
                    del items[delete-1]
            except ValueError:
                print("You need to enter a number\n")


