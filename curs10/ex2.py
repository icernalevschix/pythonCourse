"""2. Declare a class that will describe a Student, it will have an attribute named
student grade and class method that will receive a list of grades and will
return a new Student objects with average of grades."""

from statistics import mean

class Student():

    def __init__(self, grade):
        self.grade = grade

    @classmethod
    def from_list(cls, grades):
        return cls(mean(grades))

st1 = Student.from_list([10,9,7.5,8.5,9,9])
print(st1.grade)