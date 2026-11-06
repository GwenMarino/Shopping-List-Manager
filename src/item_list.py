items = []


def add_item():
    item_name = input("Name of the item?: ")
    item_price = int(input("How much does it cost?: "))
    item = {"Product Name": item_name.title(), "Price": f"${item_price}"}
    items.append(item)
    print(f"{item_name} added!")


def remove_item():
    delete = input("Delete which product?: ")
    for item in items:
        if item["Product Name"].lower() == delete.lower():
            items.remove(item)
            print(f"Removed {delete}.")
            return
    print(f"{delete} is not in your list.")
