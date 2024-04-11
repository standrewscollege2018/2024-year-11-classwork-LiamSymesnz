items = []
run_program = True
while run_program:
    get_choice = True
    while get_choice:
        try:
            choice = int(input(print("Menu\n========================\n1. See all items in list\n2. Add item to list\n3. Delete item from list\n")))
            if choice >= 4 or choice <= 0:
                print("You need to enter a valid number")
                get_choice = False
        except ValueError:
            print("Enter a valid number\n")

    if choice == 1:
        if len(items) == 0:
            print("You cant print anything, theres nothing in your list\n")
        else:
            for i in (len(items)):
                print(f"{i+1} {items[i][0]}")
    elif choice == 2:
        add = True
        while add:
            try:
                add_item = input("What item do you want to add?")
                if add_item.strip() == "":
                    print("You need an input\n")
                else:
                    items.append(add_item)
                    add = False

            except ValueError:
                    print("Enter a valid input")


    else:
        if len(items) == 0:
            print("You cant delete anything, theres nothing in the list")
        else:
            for i in (len(items)):
                print(f"{i+1} {items[i][0]}")
            delete = input("What item do you want to delete? (enter the number relevant")
            del items[delete-1]


