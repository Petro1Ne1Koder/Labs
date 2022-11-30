class Rational:

	def __init__(self, numerator=1, denominator=1):
		if denominator==0:
			raise ZeroDivisionError
		if not isinstance(numerator,int) or not isinstance(denominator,int):
			raise TypeError
		self.__numerator=numerator
		self.__denominator=denominator
		self.__reduct_rational()

	def __str__(self):
		return str(self.__numerator)+'/'+str(self.__denominator)+'='+str(float(self.__numerator/self.__denominator))

	def __add__(self, other):
		if isinstance(other, Rational):
			numerator=int(self.__numerator*other.__denominator+other.__numerator*self.__denominator)
			denominator=int(self.__denominator*other.__denominator)
			return Rational(numerator,denominator)
		elif isinstance(other,int):
			numerator=int(self.__numerator+other*self.__denominator)
			denominator=int(self.__denominator)
			return Rational(numerator,denominator)
		return NotImplemented

	def __sub__(self, other):
		if isinstance(other, Rational):
			numerator=int(self.__numerator*other.__denominator-other.__numerator*self.__denominator)
			denominator=int(self.__denominator*other.__denominator)
			return Rational(numerator,denominator)
		elif isinstance(other,int):
			numerator=int(self.__numerator-other*self.__denominator)
			denominator=int(self.__denominator)
			return Rational(numerator,denominator)
		return NotImplemented

	def __mul__(self, other):
		if isinstance(other, Rational):
			numerator=int(self.__numerator*other.__numerator)
			denominator=int(self.__denominator*other.__denominator)
			return Rational(numerator,denominator)
		elif isinstance(other,int):
			numerator=int(self.__numerator*other)
			return Rational(numerator,self.__denominator)
		return NotImplemented

	def __truediv__(self, other):
		if isinstance(other, Rational):
			numerator=int(self.__numerator*other.__denominator)
			denominator=int(self.__denominator*other.__numerator)
			return Rational(numerator,denominator)
		elif isinstance(other,int):
			denominator=int(self.__denominator*other)
			return Rational(self.__numerator,denominator)
		return NotImplemented

	def __lt__(self, other):
		if isinstance(other, Rational):
			return self.__numerator*other.__denominator<other.__numerator*self.__denominator
		elif isinstance(other,int):
			return self.__numerator<other*self.__denominator
		return NotImplemented

	def __gt__(self, other):
		if isinstance(other, Rational):
			return self.__numerator*other.__denominator>other.__numerator*self.__denominator
		elif isinstance(other,int):
			return self.__numerator>other*self.__denominator
		return NotImplemented

	def __eq__(self, other):
		if isinstance(other, Rational):
			return self.__numerator*other.__denominator==other.__numerator*self.__denominator
		elif isinstance(other,int):
			return self.__numerator==other*self.__denominator
		return NotImplemented

	def __reduct_rational(self):
		i=1	
		while i <= self.__numerator or i<= self.__denominator:
			if not self.__numerator % i and not self.__denominator % i:
				self.__numerator=self.__numerator/i
				self.__denominator=self.__denominator/i
			i=i+1
		return self

first=Rational(2, 4)
second=Rational(3, 4)
print('first: '+str(first)+'\nsecond: '+str(second))
add=first+second
sub=first-second
mul=first*second
div=first/second
print("+:\n"+'first'+" + "+'second'+" = "+str(add))
print("-:\n"+'first'+" - "+'second'+" = "+str(sub))
print("*:\n"+'first'+" * "+'second'+" = "+str(mul))
print("/:\n"+'first'+" / "+'second'+" = "+str(div))
if first<second:
	print("==:\n"+str(first)+" is lower than "+str(second)+'\n')
elif first>second:
    print("==:\n"+str(first)+" is higher than "+str(second)+'\n')
