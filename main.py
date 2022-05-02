from menu_item import MenuItem
from foods import Foods
from drinks import Drinks

food1 = Foods('Cookie', 2, 50)
food2 = Foods('Cake', 2, 100)
food3 = Foods('Pancake', 5, 250)
food4 = Foods('Bread', 3, 120)

drink1 = Drinks('Coffee', 3, 100)
drink2 = Drinks('Juice', 4, 200)
drink3 = Drinks('Milk', 3, 250)
drink4 = Drinks('Tea', 2, 150)

foods = [food1, food2, food3, food4]
drinks = [drink1, drink2, drink3, drink4]
index = 1

for food in foods:
    print(str(index) +'. ' +food.info())
    index+=1
print('-------------------------------------------------')
index = 1    
for drink in drinks:
    print(str(index) +'. ' +drink.info())
    index+=1
    
order = int(input('Input Food Number : '))
selected_food = foods[order-1]

order = int(input('Input Drink Number : '))
selected_drink = drinks[order-1]

print('You choose: ' +selected_food.name +' and ' +selected_drink.name)

diskon = int(input('How Many Packet do you Want? (10% off for 3 or more order items): '))

total_price = selected_food.get_total_price(diskon) + selected_drink.get_total_price(diskon)

print('Total price: ' +str(total_price) +'$')