from menu_item import MenuItem

menu_item1 = MenuItem('Orange', 2)
menu_item2 = MenuItem('Apple', 2)
menu_item3 = MenuItem('Durian', 5)
menu_item4 = MenuItem('Grape', 3)

menu_items = [menu_item1,menu_item2,menu_item3,menu_item4]
index = 1

for menu_item in menu_items:
    print(str(index) +'. ' +menu_item.info())
    index+=1
    
order = int(input('Input menu number : '))
selected_menu = menu_items[order-1]
print('You choose: ' +selected_menu.name)

diskon = int(input('Total order (10% off for 3 or more order items): '))

total_price = selected_menu.get_total_price(diskon)

print('Total price: ' +str(total_price))