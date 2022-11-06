class Rectangle:

    def __init__(self,width=1,length=1):
        self.width = width
        self.length = length

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    @width.setter
    def width(self, width):
        if not (isinstance(width, (float, int))):
            raise TypeError("Width isn't a number")
        if width <= 0 or width > 20:
            raise ValueError("Width not in range [0,20]");
        self.__width = width

    @length.setter
    def length(self,length):
        if not (isinstance(length, (float, int))):
            raise TypeError("Length isn't a number")
        if length <= 0 or length > 20:
            raise ValueError("Length not in range [0,20]");
        self.__length = length

    def perimeter(self):
        return 2 * (self.__width + self.__length)

    def area(self):
        return self.__width * self.__length

@staticmethod
def check_value(value):
    if value <= 0 or value > 20:
      raise Exception

square=Rectangle()
square.width=2
square.length=1
print("width and length:",str(square.width)+' '+str(square.length),"\nperimeter: ",square.perimeter(),"\narea: ",square.area())

