'''2. Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, 
    and methods like add_item_to_menu, book_tables, and customer_order.
    
    Perform the following tasks now:
	Now add items to the menu.
	Make table reservations.
	Take customer orders.'''

class Restaurant:
    
    menu_items = {1 : "Idly", 2 : "Dosa", 3 : "Briyani", 4 : "Meals", 5 : "Pongal"}
    tables = {"T1" : "Available", "T2" : "Available", "T3" : "Available", "T4" : "Reserved", "T5" : "Available"}
    orders = {}
    
    def add_menu(cls, *new_values):
        
        for new_value in new_values:
            if new_value not in cls.menu_items.values():
                new_key = len(cls.menu_items) + 1
                cls.menu_items[new_key] = new_value
            else:
                print("Already Exists")        
        print(cls.menu_items, "\n")
    
    def book_table(cls):
        
        for table_no, status in cls.tables.items():
            if status == "Available":
                print(f"{table_no} is Available")
            else:
                print(f"{table_no} is Reserved")
            
        while True:
            
            select_table = input("\nEnter your Table No : ")
            
            if select_table == table_no and status == "Reserved":
                print(f"Sorry, This Table : {select_table} is Already booked \nPlease Check table_number and Try with another")
            else:
                cls.tables[table_no] = "Reserved"
                print(f"Table : {select_table} is booked by Yourself")
                
                
            condition = input("\nDo you want to continue Table booking \nEnter ('Yes'/'Y') or ('No'/'N') : ")
                
            if condition.lower() == "no" or condition.lower() == "n":
                break
            
    def food_order(cls):
        
        print(f"\nThese are the Available Foods : \n{cls.menu_items}")
            
        while True:
                
            customer_order = int(input("\nEnter your Requirements from the above list : "))
                
            if customer_order in cls.menu_items.keys():
                print(f"\nYou're ordered : {cls.menu_items[customer_order]}")
            else:
                print(f"\nSorry, {cls.menu_items[customer_order]} unavailable choose existing one.")
                    
            order_condition = input("\nDo you want to continue Table booking \nEnter ('Yes'/'Y') or ('No'/'N') : ")
            
            if order_condition.lower() == "no" or order_condition.lower() == "n":
                print (f"\nThank you for your orders\n")
                break 
            
restaurant = Restaurant()
restaurant.add_menu("Vada", "Poori")
restaurant.book_table()
restaurant.food_order()

