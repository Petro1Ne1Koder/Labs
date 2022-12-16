import json
from abc import ABC, abstractmethod
import os


class ICourse(ABC):
    
    @property
    @abstractmethod
    def course_name(self): pass

    @course_name.setter
    @abstractmethod
    def course_name(self, course_name): pass

    @property
    @abstractmethod
    def teacher(self): pass

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher): pass

    @property
    @abstractmethod
    def program(self): pass

    @program.setter
    @abstractmethod
    def program(self, program): pass

    @abstractmethod
    def __str__(self): pass

class ITeacher(ABC):
    
    @property
    @abstractmethod
    def name(self): pass

    @name.setter
    @abstractmethod
    def name(self, name): pass

    @property
    @abstractmethod
    def courses(self): pass

    @abstractmethod
    def __str__(self): pass

class ILocalCourse(ABC):
    
    @property
    @abstractmethod
    def auditory(self): pass

    @auditory.setter
    @abstractmethod
    def auditory(self, auditory): pass

class IOffsiteCourse(ABC):
    
    @property
    @abstractmethod
    def address(self): pass

    @address.setter
    @abstractmethod
    def address(self, address): pass

class ICourseFactory(ABC):
    
    @abstractmethod
    def get_info(self): pass


class Teacher(ITeacher):
    
    staff_members = []

    def __init__(self, name):
        self.name = name["name"]
        self.__courses = []
        Teacher.staff_members.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.__name = name

    @property
    def courses(self):
        return self.__courses

    def add_course(self, courses):
        self.__courses.append(courses)

    def __str__(self):
        return f'Teacher is {self.name}, teaches {[elem.course_name for elem in self.courses]}'

    @classmethod
    def get_teacher(cls, name):
        for vals in cls.staff_members:
            if vals.name == name:
                return vals
        raise ValueError

class Course(ICourse):
    
    def __init__(self, data):
        self.course_name = data["name"]
        self.teacher = Teacher.get_teacher(data["teacher"])
        self.program = data["program"]
        self.teacher.add_course(self)

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, course_name):
        if not isinstance(course_name, str):
            raise TypeError
        self._course_name = course_name

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError
        self._teacher = teacher

    @property
    def program(self):
        return self._program

    @program.setter
    def program(self, program):
        if not all(isinstance(vals, str) for vals in program):
            raise TypeError
        self._program = program

    def __str__(self):
        return f'Course {self.course_name} teached by {self.teacher.name}. Program is: {self.program}'

class LocalCourse(ILocalCourse, Course):
    
    def __init__(self, auditory):
        super().__init__(auditory)
        self.auditory = auditory["auditory"]

    @property
    def auditory(self):
        return self._auditory

    @auditory.setter
    def auditory(self, auditory):
        if not isinstance(auditory, str):
            raise TypeError
        self._auditory = auditory

    def __str__(self):
        return super().__str__() + f' teached in {self.auditory}'

class OffsiteCourse(IOffsiteCourse, Course):
    
    def __init__(self, address):
        super().__init__(address)
        self.address = address["address"]

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if not isinstance(address, str):
            raise TypeError
        self._address = address

    def __str__(self):
        return super().__str__() + f' is located at {self.address}'

class CourseFactory(ICourseFactory):
    
    def __init__(self, file):
        if not os.path.isfile(file):
            raise ValueError
        with open(file, "r") as finp:
            self.b = json.load(finp)

    def get_info(self):
        data = self.b[0]
        self.b.pop(0)
        match data.get("type"):
            case "local":
                return LocalCourse(data)
            case "offsite":
                return OffsiteCourse(data)
            case "teacher":
                return Teacher(data)
            case _:
                raise ValueError


def main():
    file = 'note.json'
    b = CourseFactory(file)
    x = b.get_info()
    x1 = b.get_info()
    x2 = b.get_info()
    x3 = b.get_info()
    print(x)
    print(x1)
    print(x2)
    print(x3)

if __name__ == '__main__':
    main()