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

    def ToFullString(self):
        return f"Предмет: {self.subject}, Оценка: {self.grade}, Дата экзамена: {self.exam_date}"


class Person:
    def __init__(self, first_name="", last_name="", birth_date=datetime(2000, 1, 1)):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def ToFullString(self):
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

    def AddExams(self, *exams):
        self.exams.extend(exams)

    def ToFullString(self):
        exams_info = ", ".join(exam.ToFullString() for exam in self.exams)
        return f"{self.person.ToFullString()}, Образование: {self.education.name}, " \
               f"Номер группы: {self.group_number}, Экзамены: {exams_info}"

    def ToShortString(self):
        return f"{self.person.first_name} {self.person.last_name}, " \
               f"Образование: {self.education.name}, Номер группы: {self.group_number}, " \
               f"Средний балл: {self.average_grade:.2f}"


# Пример использования классов:
if __name__ == "__main__":
    student1 = Student()
    print(student1.ToShortString())

    student1.person.first_name = "Иван"
    student1.person.last_name = "Иванов"
    student1.person.birth_date = datetime(1990, 5, 15)
    student1.education = Education.Specialist
    student1.group_number = 12345

    exam1 = Exam("Математика", 95, datetime(2023, 1, 10))
    exam2 = Exam("Физика", 87, datetime(2023, 1, 15))

    student1.AddExams(exam1, exam2)
    print(student1.ToFullString())

    print(student1.ToShortString())
