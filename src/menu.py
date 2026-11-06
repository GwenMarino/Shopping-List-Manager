import item_list


def show_menu():
    is_running = True
    while is_running:
        print("")
        print("Make List:")
        print("1. Add Item: ")
        print("2. Remove Item: ")
        print("3. Show List: ")
        print("4. New List: ")
        print("5. Close Shopping List: ")
        menu_selection = int(input("Make a selection: "))
        print("")

        if menu_selection == 1:
            item_list.add_item()
        if menu_selection == 2:
            item_list.remove_item()
        if menu_selection == 3:
            print(item_list.items)
            is_running = True
        if menu_selection == 4:
            item_list.items.clear()
        if menu_selection == 5:
            print("Shopping List:")
            print(item_list.items)
            is_running = False
