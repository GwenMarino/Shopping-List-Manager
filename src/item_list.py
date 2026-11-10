items = []


def add_item():
    item_name = input("Name of the item?: ").strip()

    for item in items:  # only updates price if this item has not been listed before
        if item["name"].lower() == item_name.lower():
            item_quantity = int(input("How many?: "))
            item["quantity"] += item_quantity
            print(f"Updated {item['name']}: now {item['quantity']} on your list.")
            return
    while True:
        try:
            item_price = float(input("How much does it cost?: "))
            break
        except ValueError:
            print("Invalid input.")  # makes sure the inputs are not strings

    while True:
        try:
            item_quantity = int(input("How many?: "))
            break
        except ValueError:
            print("Invalid input.")

    items.append(
        {
            "name": item_name,
            "price": item_price,  # item structure
            "quantity": item_quantity,
        }
    )
    print(
        f"Added {item_quantity} {item_name} at ${item_price:.2f} each to your shopping list!"  # confirmation that the product was added
    )


def remove_item():
    delete = input("Delete which product?: ").strip()
    for item in items:
        if item["name"].lower() == delete.lower():
            items.remove(
                item
            )  # Removes based on the name of the item, and returns invalid if the item is not on the list
            print(f"Removed {delete}.")
            return
    print(f"{delete} is not in your list.")


def print_list():
    print("Your Shopping List:")
    total_items = 0
    total_price = 0.00

    for item in items:
        line_total = item["price"] * item["quantity"]
        if item["quantity"] == 1:
            print(f"- {item['quantity']} {item['name'].lower()}: ${line_total:.2f}")
        if item["quantity"] > 1:
            print(f"- {item['quantity']} {item['name'].lower()}'s: ${line_total:.2f}")
        total_items = sum(item["quantity"] for item in items)
        total_price += line_total
    print("")
    print(f"Total Items: {total_items}")
    print(f"Total Price: {total_price:.2f}")
