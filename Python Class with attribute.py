# Write a Python class Inventory with attributes like item_id, item_name, stock_count, and
# price, and methods like add_item, update_item, remove_item, show_item_list and
# check_an_item_details.
# Use a dictionary to store the item details, where the key is the item_id and the value is a
# dictionary containing the item_name, stock_count, and price.

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        if item_id not in self.items:
            self.items[item_id] = {"item_name": item_name, "stock_count": stock_count, "price": price}
        else:
            print("Item ID already exists.")

    def update_item(self, item_id, new_details):
        if item_id in self.items:
            self.items[item_id].update(new_details)
        else:
            print("Item ID does not exist.")

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
        else:
            print("Item ID does not exist.")

    def show_item_list(self):
        print("Item ID\tItem Name\tStock Count\tPrice")
        for item_id, details in self.items.items():
            print(f"{item_id}\t{details['item_name']}\t{details['stock_count']}\t\t{details['price']}")

    def check_an_item_details(self, item_id):
        if item_id in self.items:
            print(f"Item ID: {item_id}, Details: {self.items[item_id]}")
        else:
            print("Item ID does not exist.")

inventory = Inventory()
inventory.add_item("101", "Laptop", 10, 800)
inventory.add_item("102", "Phone", 20, 600)
inventory.show_item_list()

inventory.update_item("101", {"stock_count": 12})
inventory.remove_item("103")
inventory.show_item_list()

inventory.check_an_item_details("102")
