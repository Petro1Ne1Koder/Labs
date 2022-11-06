class Product:
    
    def __init__(self, price, description, dimensions):
        if not isinstance(price, (float, int)):
            raise TypeError("Price isn't a number");
        if price < 0:
            raise ValueError
        self.price = price
        self.description = description
        self.dimensions = dimensions
        
    def __str__(self):
        return f'The price of {self.description} {self.dimensions} is {self.price}'
        
class Customer:
    
    def __init__(self,surname, name, patronymic, mobile_phone):
        if not isinstance(mobile_phone, (int)):
            raise TypeError("Mobile phone isn't a number")
        self.surname=surname
        self.name=name
        self.patronymic=patronymic
        self.mobile_phone=mobile_phone
        
    def __str__(self):
        return f'The customer is {self.surname} {self.name} {self.patronumic}, phonenumber is {self.mobile_phone}'

class Order:

    def __init__(self, customer, *product):
        if not isinstance(customer, Customer):
            raise TypeError("There is no customer")
        for i in product:
            if not isinstance(i, Product):
                raise TypeError("There is not only products")
        self.customer = customer
        self.products = []
        self.products_quantity = []
        for i in product:
            self.Product_addition(i)
        self.value = 0
        
    def Product_addition(self, product):
        if product in self.products:
            self.products_quantity[self.products.index(product)] += 1
        else:
            self.products.append(product)
            self.products_quantity.append(1)

    def show_value(self):
        self.value = 0
        for i in self.products:
            self.value += i.price * self.products_quantity[self.products.index(i)]
        return self.value

    def __str__(self):
        return f'The price of order for {self.customer.surname} {self.customer.name} {self.customer.patronymic} is {self.show_value()}'
    
Visitor = Customer("Daniil", "Hryshai", "Dmitrovich", 123456789023)
Joystick = Product(500, "Joystick", (50, 20, 15))
Apple = Product(25, "Apple", (5, 6, 5))
order = Order(Visitor)
order.Product_addition(Joystick)
order.Product_addition(Apple)
print(Joystick)
print(Apple)
print(order)