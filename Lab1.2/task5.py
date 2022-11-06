MAX_STUDENTS = 20

class Student:

	def __init__(self, surname, name, *grades):
		if not isinstance(grades, tuple):
				raise TypeError
		for i in range(len(grades)):
			if not isinstance(grades[i], (float, int)):
				if grades[i].isdigit():
					grades[i] = float(grades[i])
				else:
					raise TypeError("Wrong number")
			elif grades[i] < 0 or grades[i] > 5:
				raise RuntimeError("Wrong grade")
		self.name = name
		self.surname = surname
		self.grades = grades

	def __str__(self):
		return self.surname+', '+self.name+', grades:'+','.join(str(i) for i in \
      self.grades)+'; avarage score='+str(self.get_average_score())

	def get_average_score(self):
		return sum(self.grades) / len(self.grades)

class Group:

	def __init__(self, *students):
		self.students=students
		self.best_students=[['','',0],['','',0],['','',0],['','',0],['','',0]]

	def __str__(self):
		return '\n'.join(str(i) for i in self.students)

	def show_best_students(self):
		for i in range(len(self.students)):
			index=0
			previous_student=['','',0]
			for j in range(len(self.best_students)):
				if self.students[i].get_average_score() > self.best_students[j][2] and index == 0:
					self.best_students[j], previous_student = previous_student, self.best_students[j]
					self.best_students[j][0] = self.students[i].surname
					self.best_students[j][1] = self.students[i].name
					self.best_students[j][2] = self.students[i].get_average_score()
					index=1
				elif index==1:
					self.best_students[j], previous_student = previous_student,self.best_students[j]
		return '\n'.join(','.join(str(item) for item in group) for group in self.best_students)+'\n'

student1 = Student("Ivanovov", "Petro", 1, 4, 4, 3, 4)
student2 = Student("Zepeli", "Jairo", 5, 5, 4, 2, 4)
student3 = Student("Jiovana", "Jorno", 2, 4, 3, 3, 5)
student4 = Student("Jostar", "Joseph", 5, 5, 4, 4, 3)
student5 = Student("Bithmark", "Joseph", 2, 3, 3, 4, 3)
student6 = Student("Kujo", "Jotaro", 5, 4, 3, 3, 2)
student7 = Student("Higashikata", "Josuke", 5, 3, 3, 4, 4)
student8 = Student("Petrov", "Ivan", 2, 3, 2, 4, 3)
student9 = Student("Cujoh", "Jolune", 4, 2, 4, 3, 4)
student10 = Student("Joestar", "Jonny", 5, 3, 3, 4, 3)
student11 = Student("Brando", "Dio", 5, 5, 5, 4, 5)
student12 = Student("Hryshai", "Daniel", 4, 3, 4, 3, 3)
student13 = Student("Pinchuk", "Alexander", 4, 4, 5, 4, 3)
student14 = Student("Kaverin", "Vlad", 4, 5, 3, 4, 3)
student15 = Student("Oksyukovsky", "Oleh", 4, 4, 5, 3, 2)
student16 = Student("Mister", "Alien", 2, 4, 4, 2, 3)
student17 = Student("Bocharov", "Vadim", 3, 4, 4, 4, 3)
student18 = Student("Kirkorov", "Filip", 4, 4, 4, 3, 5)
student19 = Student("Iglesias", "Gabriel", 4, 4, 5, 3, 2)
student20 = Student("Potter", "Harry", 4, 4, 2, 3, 5)
group = Group(student1, student2, student3, student4, student5, student6, student7, student8, student9, student10, 
	student11, student12, student13, student14, student15, student16, student17, student18, student19, student20)
print("Top 5 students:\n"+group.show_best_students())