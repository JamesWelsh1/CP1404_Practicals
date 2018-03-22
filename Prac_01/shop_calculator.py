"""
Number of items:3
Price of item: 100
Price of item: 21.56
Price of item: 3
Total price for 3 items is $112.10
"""
Total_price = 0
No_items = int(input(">>> Number of items: "))
if No_items < 0:
    print("Invalid Number of Items")
else:
    for i in range(No_items,0,-1):
        Item_price = float(input("Price of Item: $"))
        Total_price += Item_price
    if Total_price > 100:
        Total_price *=0.9
    print("Total Price for", No_items, "Items is: $", Total_price)
