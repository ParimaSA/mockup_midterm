from mockup_class import Coffee, Smoothie, Tea, CoffeeMenu, SmoothieMenu, TeaMenu, Menu

t1 = Tea("Green Tea", 0.6, 0.4, ['Orange'], 100.0)
print(t1.info())

t1.__sub__("Orange")
print(t1.info())

t1.__add__("Strawberry")
t1.__add__("Chocolate")
print(t1.info())

t2 = Tea("Red Tea", 0.8, 0.2, [], 150.0)

tea_menu = TeaMenu()
smoothie_menu = SmoothieMenu()
coffee_menu = CoffeeMenu()
menu = Menu(coffee_menu, smoothie_menu, tea_menu)
tea_menu.__add__(t1)
tea_menu.__add__(t2)
print()
print(tea_menu.tea_info())

s1 = Smoothie("Banana Smoothie", 0.9, 0.1, [], 200.0)
smoothie_menu.__add__(s1)

coffee_menu.__add__(Coffee("Latte", 0.5, 0.5, [], 60.0))

print()
print(menu.all_menu_info())