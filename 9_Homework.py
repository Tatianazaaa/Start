class Gypsum:
    def __init__(self, name, height, width, length, price):
        self.name = name
        self.height = height
        self.width = width
        self.length = length
        self.price = price

    def __str__(self):
        return f"{self.name}: высота {self.height} см,  ширина {self.width} см, длина {self.length} см. Стоимость: {self.price} руб."

# Кашпо
class Pots:
    def __init__(self, name, height, width, length, price):
        super().__init__(name, height, width, length, price)

pots = Gypsum('Кашпо', 8.5, 9, 9, 294)
pots.__str__()
print(pots.__str__())

# Поднос
class Tray:
    def __init__(self, name, height, width, length, price):
        super().__init__(name, height, width, length, price)

tray = Gypsum('Поднос', 1.5, 8.5, 18, 300)
tray.__str__()
print(tray.__str__())

# Шкатулка
class Casket:
    def __init__(self, name, height, width, length, price):
        super().__init__(name, height, width, length, price)

casket = Gypsum('Шкатулка', 9, 8, 8, 550)
casket.__str__()
print(casket.__str__())

# Набор (Поднос + шкатулка)
class Set(Casket, Tray):
    def __init__(self, set_name):
        self.set_name = set_name
        #super().__init__(height, width, length, price)
        self.height = tray.height + casket.height
        self.width = tray.width
        self.length = tray.length
        self.price = (tray.price + casket.price)*0.9

    def __repr__(self):
        return f"{self.set_name}: {tray.name} и {casket.name}. Размеры набора: {self.height} см, {self.width} см, {self.length} см. Стоимость: {self.price} руб."

set = Set('Набор')
set.__repr__()
print(set.__repr__())


# С корзиной не получилось ничего придумать
class Bag:
    def __init__(self, bag_name):
        self.bag_name = bag_name
        self.price = 0
        #self.price = super().__init__(name, price)
        self.bag = []

    def add_product(self, name: Gypsum):
        self.bag.append(self.bag_name)
        self.bag += self.name
        return f'В вашей корзине: {self.name}.\n Сумма заказа: {self.price} руб. '

    def get_product(self):
        return self.bag_name



bag = Bag('Корзина')

#print(Bag)
print(bag.add_product(tray))