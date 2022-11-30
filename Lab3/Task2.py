import datetime
import calendar

MAX_MONTH=12
MIN_DAY_OR_MONTH=1
MIN_YEAR=0

class Calendar:
    
	def __init__(self, year, month, day):
		if not isinstance(day, (int, float)) or not isinstance(month,(int, float)) or not isinstance(month,(int, float)):
			raise TypeError
		if month<MIN_DAY_OR_MONTH or month>MAX_MONTH or year<MIN_YEAR or day<MIN_DAY_OR_MONTH or day>calendar.monthrange(year,month)[1]:
			raise ValueError 
		self.__day=day
		self.__month=month
		self.__year=year

	def __str__(self):
		return datetime.date(self.__year, self.__month, self.__day).strftime("%d.%m.%Y")

	def __lt__(self, other):
		if not isinstance(other, Calendar):
			raise TypeError
		if self.__year==other.__year:
			if self.__month==other.__month:
				return self.__day<other.__day
			return self.__month<other.__month
		return self.__year<other.__year

	def __le__(self, other):
		if not isinstance(other, Calendar):
			raise TypeError
		if self.__year==other.__year:
			if self.__month==other.__month:
				return self.__day<=other.__day
			return self.__month<other.__month
		return self.__year<other.__year

	def __eq__(self, other):
		if not isinstance(other, Calendar):
			raise TypeError
		return self.__year==other.__year and self.__month==other.__month and self.__day==other.__day

	def __ne__(self, other):
		if not isinstance(other, Calendar):
			raise TypeError
		return self.__year!=other.__year or self.__month!=other.__month or self.__day!=other.__day

	def __gt__(self, other):
		if not isinstance(other, Calendar):
			raise TypeError
		if self.__year==other.__year:
			if self.__month==other.__month:
				return self.__day>other.__day
			return self.__month>other.__month
		return self.__year>other.__year

	def __ge__(self, other):
		if not isinstance(other, Calendar):
			raise TypeError
		if self.__year==other.__year:
			if self.__month==other.__month:
				return self.__day>=other.__day
			return self.__month>other.__month
		return self.__year>other.__year

	def __iadd__(self, other):
		if not isinstance(other, Calendar):
			raise TypeError
		self.__year+=other.__year
		self.__month+=other.__month
		self.__day+=other.__day
		while self.__month>MAX_MONTH or self.__day>calendar.monthrange(self.__year, self.__month)[1]:
			if self.__month>MAX_MONTH:
				self.__month-=MAX_MONTH
				self.__year+=MIN_DAY_OR_MONTH
			if self.__day>calendar.monthrange(self.__year, self.__month)[1]:
				self.__day-=calendar.monthrange(self.__year, self.__month)[1]
				self.__month+=MIN_DAY_OR_MONTH
		return self


	def __isub__(self, other):
		if not isinstance(other, Calendar):
			raise TypeError
		self.__year-=other.__year
		self.__month-=other.__month
		self.__day-=other.__day
		while self.__month<MIN_DAY_OR_MONTH or self.__day<MIN_DAY_OR_MONTH:
			if self.__year<MIN_YEAR:
				raise ValueError
			if self.__month<MIN_DAY_OR_MONTH:
				self.__month+=MAX_MONTH
				self.__year-=MIN_DAY_OR_MONTH
			if self.__day<MIN_DAY_OR_MONTH:
				self.__day+=calendar.monthrange(self.__year, self.__month)[1]
				self.__month-=MIN_DAY_OR_MONTH
		return self

day1=Calendar(2022,1,31)
day2=Calendar(1987,9,29)

if day1>day2:
	print(str(day1)+" > "+str(day2)+'\n')
elif day1<day2:
	print(str(day1)+" < "+str(day2)+'\n')
if day1>=day2:
	print(str(day1)+" > or == "+str(day2)+'\n')
elif day1<=day2:
	print(str(day1)+" < or == "+str(day2)+'\n')
if day1==day2:
	print(str(day1)+" == "+str(day2)+'\n')
elif day1!=day2:
	print(str(day1)+" != "+str(day2)+'\n')
 
print(str(day1)+' + '+str(day2),end=' = ')
day1+=day2
print(str(day1)+'\n')
print(str(day1)+' - '+str(day2),end=' = ')
day1-=day2
print(str(day1))