import json
from datetime import datetime

class Insid:
    def __init__(self):
        self._doping = {
                                  "pineapple": 1.2,
                                  "mushrooms": 1.3,
                                  "chipotle": 1.5,
                                  "bacon": 1.55,
                                  "veal": 1.6,
                                  "ham": 1.65,
                                  }
        self.ingr = []
        self.dop_ingr = []
        self.name = ""
        self.price = 0

    def get_menu(self):
        return f''+ ", ".join(map(str, self._doping))
    
    def __str__(self):
        if not self.dop_ingr:
            return f"{self.name}:\nIngredients - {', '.join(map(str, self.ingr))}\nPrice - {self.final_price()}"
        else:
            return f"{self.name}:\nIngredients - {', '.join(map(str, self.ingr)) +', ' + ', '.join(map(str, self.dop_ingr))} \
                \nPrice - {self.final_price()}"

    def adding(self, *args):
        for ingredient in args:
            if not isinstance(ingredient, str):
                raise TypeError()
            if ingredient not in self._doping.keys():
                raise ValueError("We dont have this ingredient.")
            self.dop_ingr.append(ingredient)

    def final_price(self):
        return self.price + sum(self._doping[ingredients] for ingredients in self.dop_ingr)

class HawaiianPizza(Insid):
    def __init__(self):
        super().__init__()
        self.name = "Hawaiian pizza"
        self.ingr = ["pizza sauce", "mozzarella", "pineapple", "chicken"]
        self.price = 135

class MushroomPizza(Insid):
    def __init__(self):
        super().__init__()
        self.name = "Mushroom pizza"
        self.ingr = ["mushrooms", "mozzarella", "pepperoni", "Alfredo sauce"]
        self.price = 99

class MargheritaPizza(Insid):
    def __init__(self):
        super().__init__()
        self.name = "Margherita pizza"
        self.ingr = ["pizza sauce", "mozzarella"]
        self.price = 99

class MexicanPizza(Insid):
    def __init__(self):
        super().__init__()
        self.name = "Mexican pizza"
        self.ingr = ["hunting sausages", "barbecue sauce", "chipotle"]
        self.price = 195

class MeatPizza(Insid):
    def __init__(self):
        super().__init__()
        self.name = "Meat pizza"
        self.ingr = ["chicken", "pepperoni", "pizza sauce", "bacon", "veal", "ham"]
        self.price = 263

class PepperoniPizza(Insid):
    def __init__(self):
        super().__init__()
        self.name = "Pepperoni pizza"
        self.ingr = ["mozzarella", "pepperoni", "pizza sauce"]
        self.price = 135

class FourCheesesPizza(Insid):
    def __init__(self):
        super().__init__()
        self.name = "Four cheeses pizza"
        self.ingr = ["mozzarella", "parmesan", "Alfredo sauce", "cheddar", "feta"]
        self.price = 205
               
def TodaysPizza():
    with open("ChoosePizza.json") as file:
        list = json.load(file)
    return eval(list[datetime.today().strftime("%A")])()

Pizza = TodaysPizza()
print("Todays is", datetime.today().strftime("%A"), "\nWe recommend to you:\n",Pizza)
result = input("Would you like to add ingr? (yes/no)\n")
if result.lower() == "yes":
    print("\nChoose and input one from the list: ")
    print(Pizza.get_menu())
    ingr = input()
    Pizza.adding(ingr)
elif result.lower() != "no":
    raise IOError("invalid input")
print("\nYour order is:\n",Pizza)
