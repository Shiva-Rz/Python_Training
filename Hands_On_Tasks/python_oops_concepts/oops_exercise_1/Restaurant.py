'''2. Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, 
    and methods like add_item_to_menu, book_tables, and customer_order.
    
    Perform the following tasks now:
	Now add items to the menu.
	Make table reservations.
	Take customer orders.'''
  
class Restaurant:

    menu_items = {1 : "Dosa", 2 : "Idly", 3 : "Meals"}
    book_tables = {1 : "Available", 2 : "Available", 3 : "Available", 4 : "Available", 5 : "Available", 6 : "Reserved", 7 : "Available"}
    customer_orders = {}
    
    print(menu_items)
    
    @classmethod
    def add_items(cls, menu_items):
        cls.menu_items[len(cls.menu_items) + 1] = menu_items
        # present = True
        # for value in cls.menu_items.items():
        #     if value not in cls.menu_items:
        #         present = False
                
        # if present == False:
        #     new_key = len(cls.menu_items) + 1
        #     cls.menu_items[new_key] = menu_items

    @classmethod
    def book_table(cls):
        
        for table_number, status in cls.book_tables.items():
            if status == "Reserved":
                print(f"Table No : {table_number} is Reserved")
            else:
                print(f"Table No : {table_number} is Available")
        
        while True:
            
            customer_table = int(input("Enter the table no you needed :  "))
            
            if customer_table in cls.book_tables and cls.book_tables[customer_table] == "Reserved":
                print(" The Table doesn't available \nPlease choose another One.")
            else:    
               cls.book_tables[customer_table] = "Reserved"
               print(f"Table {customer_table} is booked")
            
            customer_choice = input("Do you want to continue 'yes'/ 'y' 'no'/'n'  :").lower()
            if customer_choice != "yes":
                break
    
    @classmethod           
    def customer_order(cls):
         
         while True:
            for food_id, food in cls.menu_items.items():
                print(f"{food_id}  {food} ") 
                
            customer_food = int(input("choose your required dish  : \n"))
                
            if customer_food in cls.menu_items.keys():
                print(f"Your order {cls.menu_items[customer_food]} is placed")
            else:
                print(" your order dishes is unavailable choose exists one.")
                    
            order = input("Do you want to continue yes /no  :").lower()
            
            if order != "y":
                print("Thank you ")
                print (f"your total orders are {cls.menu_items[customer_food]}")
                break 
                
restaurant = Restaurant()
restaurant.add_items("Pongal")
print(restaurant.menu_items)

restaurant.book_table()
print(restaurant.book_table)

restaurant.customer_order()
