items = []


def add_item():
    item_name = input("Name of the item?: ").strip()

    for item in items:  # only updates price if this item has not been listed before
        if item["name"].lower() == item_name.lower():
            item_quantity = int(input("How many?: "))
            item["quantity"] += item_quantity
            print(f"Updated {item['name']}: now {item['quantity']} on your list.")
            return

    item_price = float(input("How much does it cost?: "))
    item_quantity = int(input("How many?: "))
    items.append(
        {
            "name": item_name,
            "price": item_price,
            "quantity": item_quantity,
        }
    )
    print(
        f"Added {item_quantity} {item_name} at ${item_price:.2f} each to your shopping list!"
    )


def remove_item():
    delete = input("Delete which product?: ").strip()
    for item in items:
        if item["name"].lower() == delete.lower():
            items.remove(item)
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
        total_items += item["quantity"]
        total_price += line_total
    print("")
    print(f"Total Items: {total_items}")
    print(f"Total Price: {total_price:.2f}")
