class Item:
    def __init__(self,name , quantity = 0):
        # print(f"Chant and be happy : {name}")
        self.name = name
        self.quantity = quantity
    def calculate_total_price(self):
        return self.quantity * 5

item1 = Item("iphone",42)
item1.price =100
# item1.quantity =42
# print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item("home")
item2.price =1005
# item2.quantity =432
# print(item1.calculate_total_price(item2.price, item2.quantity))

print(item1.name)
print(item2.name)
print(item1.quantity)
print(item2.quantity)
print(item1.calculate_total_price())
# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))

# random_str = "abhay"

# print(random_str.upper())