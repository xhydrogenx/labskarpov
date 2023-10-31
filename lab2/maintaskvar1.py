from enum import Enum, auto
from datetime import datetime


class Education(Enum):
    Specialist = auto()
    Bachelor = auto()
    SecondEducation = auto()


class Exam:
    def __init__(self, subject="", grade=0, exam_date=datetime(2000, 1, 1)):
        self.subject = subject
        self.grade = grade
        self.exam_date = exam_date

    def to_full_string(self):
        return f"Предмет: {self.subject}, Оценка: {self.grade}, Дата экзамена: {self.exam_date}"


class Person:
    def __init__(self, first_name="", last_name="", birth_date=datetime(2000, 1, 1)):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def to_full_string(self):
        return f"Имя: {self.first_name}, Фамилия: {self.last_name}, Дата рождения: {self.birth_date}"


class Student:
    def __init__(self, person=Person(), education=Education.Bachelor, group_number=0):
        self.person = person
        self.education = education
        self.group_number = group_number
        self.exams = []

    @property
    def average_grade(self):
        if not self.exams:
            return 0.0
        total_grade = sum(exam.grade for exam in self.exams)
        return total_grade / len(self.exams)

    def add_exams(self, *exams):
        self.exams.extend(exams)

    def to_full_string(self):
        exams_info = ", ".join(exam.to_full_string() for exam in self.exams)
        return f"{self.person.to_full_string()}, Образование: {self.education.name}, " \
               f"Номер группы: {self.group_number}, Экзамены: {exams_info}"

    def to_short_string(self):
        return f"{self.person.first_name} {self.person.last_name}, " \
               f"Образование: {self.education.name}, Номер группы: {self.group_number}, " \
               f"Средний балл: {self.average_grade:.2f}"


# Пример
if __name__ == "__main__":
    student1 = Student()
    print(student1.to_short_string())

    student1.person.first_name = "Иван"
    student1.person.last_name = "Карпов"
    student1.person.birth_date = datetime(1999, 12, 8)
    student1.education = Education.Bachelor
    student1.group_number = 'PIB-01'

    exam1 = Exam("Математика", 95, datetime(2023, 1, 10))
    exam2 = Exam("Физика", 87, datetime(2023, 1, 15))

    student1.add_exams(exam1, exam2)
    print(student1.to_full_string())

    print(student1.to_short_string())
