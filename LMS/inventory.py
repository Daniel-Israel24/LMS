class ShopInventory:
    def __init__(self, name):
        self.name = name
        self.stock = []

    def add_item(self, name, stock_type, current_price, future_price, expenditure):
        """Add a new ite to the inventory."""
        self.stock.append({
            "name": name,
            "type": stock_type,
            "current_price": current_price,
            "future_price": future_price,
            "expenditure": expenditure
        })

    def display_inventory(self):
        """display current and future price for all items"""
        print(f"INVENTORY LISTING FOR {str(self.name).upper()}")
        print(f"{"item":<20} {"Type":<10} {"Current Price":15} {"Future Price":<15} {"Expenditure":<15}")
        print("-" * 75)
        for item in self.stock:
            print(f"{item["name"]:<20} {item["type"]:<10} ${item["current_price"]:<14.2f} ${item["future_price"]:<14.2f} ${item["expenditure"]:<14.2f}")
        if not len(self.stock):
            print("You have nothing in your inventory!")

    def calculate_financials(self):
        """Calculate total expenditure, potential profits, and value changes"""
        total_expenditure = 0
        current_value = 0
        future_value = 0

        for item in self.stock:
            total_expenditure += item["expenditure"]
            current_value += item["current_price"]
            future_value += item["future_price"]

        current_profit = current_value - future_value
        future_profit = future_value - total_expenditure
        value_change = future_value - current_value

        return {
            "total_expenditure": total_expenditure,
            "current_value": current_value,
            "future_value": future_value,
            "current_profit": current_profit,
            "future_profit": future_profit,
            "value_change": value_change,
        }
    def financial_summary(self):
        finances = self.calculate_financials()
        print(f"FINANCIAL SUMMARY FOR {str(self.name).upper()}:")
        print(f"Total Expenditure: ${finances['total_expenditure']:.2f}")
        print(f"current stock value: ${finances['current_value']:2f}")
        print(f"Projected value (2mo):${finances['future_value']:2f}")
        print(f"value change: ${finances['value_change']:2f}")
        print(f"current profit: ${finances['current_profit']:2f}")
        print(f"projected profit (2mo):${finances['future_profit']:2f}")
def PopulateInventory(inventory):
    try:
        name = input("Enter the item name: ")
        type = input("Enter the item type: ")
        cp = float(input("Enter the current price: "))
        fp = float(input("Enter the future price: "))
        exp = float(input("Enter the expenditure: "))
        inventory.add_item(name, type, cp, fp, exp)
        print("Successfully added the item to the inventory")
    except:
        print("Failed to add the item due to an input error!")

def demo():
    shop = ShopInventory("Demo Shop")
    shop.add_item("Laptop", "New", 1200.00, 1100.00, 900.00)
    shop.add_item("monitor", "Old", 150.00, 120.00, 80.00)
    shop.add_item("keyboard", "New", 85.00, 75.00, 50.00)
    shop.add_item("Mouse", "Old", 25.00, 18.00, 10.00)
    print("SHOP INVENTORY OVERVIEW -- Demo Shop")
    shop.display_inventory()
    shop.financial_summary()
    
def dash():
    global shop
    print("Welcome to Inventory Manager of %s" %shop.name)
    print("Please choose an action.")
    a = input("1. Add an item\n2. View items\n3. View financial Summary\n4. Run demo shop\n5. Sign Out\n6. Exit\nEnter your response: ")
    print("-"*80)
    match a:
        case "1":
            PopulateInventory(shop)
        case "2":
            shop.display_inventory()
        case "3":
            shop.financial_summary()
        case "4":
            demo()
        case "5":
            # del shop
            global shop_name
            shop_name = None
            shop = None
        case "6":
            print("Exiting the program ...")
            global shouldClose
            shouldClose = True
        case _:
            print("Invalid Input!")
def auth():
    global shop
    global shop_name
    shop_name = input("Choose a name for your shop: ")
    if len(shop_name):
        shop = ShopInventory(shop_name)
    else:
        print("Shop name must be at least 1 character long!")
        shop_name = None

shouldClose = False
shop_name = None
shop = None
while not shouldClose:
    if not shop:
        print("\nWelcome to our Inventory Management System!")
        match input("Please Choose an option.\n1. Sign In\n2. Exit\nEnter your choice: "):
            case "1":
                auth()
            case "2":
                print("Exiting the program ...")
                shouldClose = True
            case _:
                print("Invalid Input!")
        continue
    print("\n")
    print("="*80)
    dash()
exit(0)