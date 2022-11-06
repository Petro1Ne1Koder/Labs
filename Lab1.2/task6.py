class Binary_Tree:

    def __init__(self, product_code=None, price=None):
        self.left = None
        self.right = None
        self.product_code=product_code
        self.price=price

    def put_elements(self, product_code, price):
        
        if not isinstance(product_code, int):
                raise TypeError("Wrong product code")
        if price<0 or product_code<0:
            raise RuntimeError
        if not isinstance(price, (int, float)):
                raise TypeError("Wrong price")
        if self.product_code:
            if product_code < self.product_code:
                if self.left is None:
                    self.left = Binary_Tree(product_code, price)
                else:
                    self.left.put_elements(product_code, price)
            elif product_code > self.product_code:
                if self.right is None:
                    self.right = Binary_Tree(product_code, price)
                else:
                    self.right.put_elements(product_code, price)
        else:
            self.product_code=product_code
            self.price=price

    def search_elements(self,product_code,quantity):
 

        if not isinstance(product_code,int) or not isinstance(quantity,int):
                raise TypeError
        if quantity<0 or product_code<0:
            raise RuntimeError
        if product_code==self.product_code:
            return self.price*quantity
        elif product_code < self.product_code:
            if self.left is not None:
                return self.left.search_elements(product_code,quantity)
            else:
                return None
        elif product_code > self.product_code:
            if self.right is not None:
                return self.right.search_elements(product_code,quantity)
            else:
                return None
            

order = Binary_Tree()
quantity=15
order.put_elements(6,3.12)
order.put_elements(14,20)
order.put_elements(3,45.75)
order.put_elements(7,3.2)
order.put_elements(9,125.89)
if order.search_elements(14,20)!=None:
    print('Product: '+str(quantity)+" of them="+str(order.search_elements(14,quantity)))
else:
    print("there isn't product with this code")