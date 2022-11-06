import json
import itertools
from datetime import datetime


class Info:
    def __init__(self, fileind, stringind):
        with open(fileind) as file:
            self._products_data = json.load(file)
        self._stringind = stringind

    @property
    def get_info(self):
        return f"{self._products_data.items()}"

    def __str__(self):
        return "\n".join(f"{i}" for i in self._products_data[self._stringind])

class Ingridients(Info):
    def __init__(self, fileind="Ingridients.json", stringind="Ingridients"):
        super().__init__(fileind, stringind)
        self._stringind = stringind


class Pizza:
    def __init__(self):
        self._day = datetime.today().strftime("%A")
        with open("Menu.json") as file:
            pizzas = json.load(file)
        date = self._day
        for i in pizzas["Pizza"]:
            if date == i["day"]:
                self.__dict__ = i.copy()

    @property
    def get_info(self):
        return dict(itertools.islice(self.__dict__.items(), 3))

    def adding(self, product):
        self.__dict__["ingredients"].append(product["name"])
        self.__dict__["price"] += product["price"]

    def __str__(self):
        return str.join("\n", [f"{i}: {self.__dict__[i]}" for i in self.__dict__.keys() if i != "day"])


class Order:
    def __init__(self):
        with open("Menu.json") as file:
            self._pizza_menu = json.load(file)
        self._extra = Ingridients()
        self._order = Pizza()

    @property
    def get_menu(self):
        return '\n'.join([f'{i["name"]}' for i in self._extra._products_data[self._extra._stringind]])

    def change_pizza(self, product):
        if not any(product == i["name"] for i in self._extra._products_data[self._extra._stringind]):
            raise ValueError("invalid input")
        for i in self._extra._products_data[self._extra._stringind]:
            if product == i["name"]:
                self._order.adding(i)

    def make_order(self):
            info = self._order.get_info
            database = {
                "name": info["name"],
                "price": info["price"],
                "purchase_date": str(datetime.now())
            }

    @property
    def get_order_info(self):
        info = self._order.get_info
        return f'Today is: {datetime.today().strftime("%A")}\nWe recomend you: {info["name"]}\nIngredients - ' + ", ".join([f"{i}" for i in info["ingredients"]]) +\
               f'\nPrice - {info["price"]}'

    def __str__(self):
        return f'Your order is:\n{self._order}'


your_order = Order()
print(your_order.get_order_info)
result = input("Would you like to add ingredients? (yes/no)\n")
if result.lower() == "yes":
    print("Choose and input one from the list")
    print(your_order.get_menu)
    your_order.change_pizza(input())
elif result.lower() != "no":
    raise IOError("invalid input")

your_order.make_order()
print(your_order)