class Rational:

	def __init__(self,numerator=1,denominator=1):
		if denominator==0:
			raise ZeroDivisionError
		if not isinstance(numerator,int) or not isinstance(denominator,int):
			raise TypeError("Wrong arguments")

		i=1	
		while i <= numerator or i<= denominator:
			if not numerator % i and not denominator % i:
				numerator=numerator/i
				denominator=denominator/i
				i=1
			i=i+1
		self.__numerator=int(numerator)
		self.__denominator=int(denominator)

	def __add__(self,other):
		if not isinstance(other,Rational):
			raise TypeError
		numerator=self.__numerator*other.__denominator+other.__numerator*self.__denominator
		denominator=self.__denominator*other.__denominator
		return Rational(numerator,denominator)

	def __sub__(self,other):
		if not isinstance(other,Rational):
			raise TypeError
		numerator=self.__numerator*other.__denominator-other.__numerator*self.__denominator
		denominator=self.__denominator*other.__denominator
		return Rational(numerator,denominator)

	def __mul__(self,other):
		if not isinstance(other,Rational):
			raise TypeError
		numerator=self.__numerator*other.__numerator
		denominator=self.__denominator*other.__denominator
		return Rational(numerator,denominator)

	def __truediv__(self,other):
		if not isinstance(other,Rational):
			raise TypeError
		numerator=self.__numerator*other.__denominator
		denominator=self.__denominator*other.__numerator
		return Rational(numerator,denominator)

	def show_standart(self):
		return str(self.__numerator)+'/'+str(self.__denominator)

	def show_float(self):
		return str(float(self.__numerator/self.__denominator))

first=Rational(1,4)
second=Rational(3,4)
add=first+second
sub=first-second
mul=first*second
div=first/second
print("+:\n"+first.show_standart()+" + "+second.show_standart()+" = "+add.show_standart()+'\n'+
	first.show_float()+" + "+second.show_float()+" = "+add.show_float())
print("-:\n"+first.show_standart()+" - "+second.show_standart()+" = "+sub.show_standart()+'\n'+
	first.show_float()+" - "+second.show_float()+" = "+sub.show_float())
print("*:\n"+first.show_standart()+" * "+second.show_standart()+" = "+mul.show_standart()+'\n'+
	first.show_float()+" * "+second.show_float()+" = "+mul.show_float())
print("/:\n"+first.show_standart()+" / "+second.show_standart()+" = "+div.show_standart()+'\n'+
	first.show_float()+" / "+second.show_float()+" = "+div.show_float())