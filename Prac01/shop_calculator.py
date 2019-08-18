number_of_items = int(input("How many items?"))
price_of_item = 0
total_items = 0

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("How many items?"))
else:
    total_items += number_of_items
    while number_of_items > 0:
        price_of_item += float(input("Price of item?"))
        number_of_items -= 1
    else:
        if price_of_item > 100:
            print("Total price of %d items is $%s" % (total_items, price_of_item * .9))
        else:
            print("Total price of %d items is $%s" % (total_items, price_of_item))
