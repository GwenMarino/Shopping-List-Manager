import item_list


def show_menu():
    is_running = True
    while is_running:
        print("")
        print("Menu:")
        print("1. Add Item: ")
        print("2. Remove Item: ")
        print("3. Show List: ")
        print("4. New List: ")
        print("5. Close Shopping List: ")
        menu_selection = input("Make a selection: ")
        print("")

        if menu_selection == "1":
            item_list.add_item()
        elif menu_selection == "2":
            item_list.remove_item()
        elif menu_selection == "3":
            item_list.print_list()
            is_running = True
        elif menu_selection == "4":
            item_list.items.clear()
        elif menu_selection == "5":
            print("Shopping List:")
            item_list.print_list()
            is_running = False
        else:
            print("Invalid Option")


# The menu_selection can be a string as opposed to an int because we aren't actually doing anything with the numerical value,
# we are simply using them for options. Changing them to a string makes it so that a string input or an int input doesn't give us errors.
